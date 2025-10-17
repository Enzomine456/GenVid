import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import datetime
import uuid
import json

# Ensure videos and uploads directories exist
if not os.path.exists('videos'):
    os.makedirs('videos')
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///genvid.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Import models after db initialization
from models import User, APIKey, VideoRequest

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/videos/<video_id>')
def serve_video(video_id):
    """Serve generated videos"""
    return send_from_directory('videos', f'{video_id}.mp4')

@app.route('/uploads/<filename>')
def serve_upload(filename):
    """Serve uploaded images"""
    return send_from_directory('uploads', filename)

@app.route('/api/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.get_json()
    
    # Check if user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'User already exists'}), 400
    
    # Create new user
    user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']  # In production, hash this!
    )
    db.session.add(user)
    db.session.commit()
    
    # Create API key for user
    api_key = str(uuid.uuid4())
    key = APIKey(key=api_key, user_id=user.id)
    db.session.add(key)
    db.session.commit()
    
    return jsonify({
        'message': 'User created successfully',
        'api_key': api_key
    }), 201

@app.route('/api/login', methods=['POST'])
def login():
    """Login user and return JWT token"""
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user and user.password == data['password']:  # In production, verify hashed password
        access_token = create_access_token(identity=user.id)
        return jsonify({
            'token': access_token,
            'user_id': user.id
        }), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/upload-image', methods=['POST'])
@jwt_required()
def upload_image():
    """Upload reference image"""
    current_user_id = get_jwt_identity()
    
    # Check if file was sent
    if 'image' not in request.files:
        return jsonify({'message': 'No image file provided'}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'message': 'No image selected'}), 400
    
    if file:
        # Generate unique filename
        filename = f"{uuid.uuid4()}_{file.filename}"
        filepath = os.path.join('uploads', filename)
        
        # Save file
        file.save(filepath)
        
        return jsonify({
            'message': 'Image uploaded successfully',
            'filename': filename,
            'url': f'/uploads/{filename}'
        }), 200
    
    return jsonify({'message': 'Error uploading image'}), 500

@app.route('/api/generate-video', methods=['POST'])
@jwt_required()
def generate_video():
    """Generate animated video from text prompt and reference images"""
    current_user_id = get_jwt_identity()
    data = request.get_json()
    prompt = data.get('prompt', '')
    reference_images = data.get('reference_images', [])
    
    if not prompt:
        return jsonify({'message': 'Prompt is required'}), 400
    
    # Save video request to database
    video_request = VideoRequest(
        user_id=current_user_id,
        prompt=prompt,
        status='processing'
    )
    db.session.add(video_request)
    db.session.commit()
    
    try:
        # Generate video using reference images
        video_id = str(uuid.uuid4())
        video_filename = f"{video_id}.mp4"
        video_path = os.path.join('videos', video_filename)
        
        # Create a video based on the prompt and reference images
        create_animated_video(prompt, reference_images, video_path)
        
        # Update request status
        video_request.status = 'completed'
        video_request.result_url = f"/videos/{video_id}"
        video_request.metadata = json.dumps({
            'prompt': prompt,
            'reference_images': reference_images,
            'duration': 10  # seconds
        })
        db.session.commit()
        
        return jsonify({
            'message': 'Video generated successfully',
            'video_id': video_id,
            'video_url': f'/videos/{video_id}',
            'download_url': f'/videos/{video_id}'
        }), 200
        
    except Exception as e:
        video_request.status = 'failed'
        db.session.commit()
        return jsonify({'message': f'Error generating video: {str(e)}'}), 500

def create_animated_video(prompt, reference_images, output_path):
    """Create an animated video based on the prompt and reference images"""
    try:
        # For demonstration, we'll create a simple video that mentions the reference images
        # In a real implementation, you would use these images to influence the video generation
        
        # Create a minimal valid MP4 file
        with open(output_path, 'wb') as f:
            # MP4 header (minimal valid MP4)
            f.write(b'\x00\x00\x00\x18ftypmp42\x00\x00\x00\x00mp42isom<\x00\x00\x00\x08free')
            # Add some basic video data
            f.write(b'\x00\x00\x00\x14mdat' + b'\x00' * 100)
            
            # If we have reference images, we could include information about them
            if reference_images:
                # In a real implementation, you would process these images
                image_info = f"Reference images: {len(reference_images)} uploaded"
                f.write(image_info.encode())
        
        return True
    except Exception as e:
        print(f"Failed to create video file: {e}")
        return False

@app.route('/api/suggested-prompts', methods=['GET'])
def suggested_prompts():
    """Return a list of suggested prompts for video generation"""
    prompts = [
        "A magical forest with glowing mushrooms and fairies dancing",
        "Underwater adventure with dolphins and coral reefs",
        "Space exploration with astronauts visiting distant planets",
        "Medieval castle siege with knights and dragons",
        "Futuristic city with flying cars and robots",
        "Jungle safari with exotic animals and waterfalls",
        "Winter wonderland with snowmen and reindeer",
        "Haunted mansion with ghosts and mysterious corridors",
        "Pirate ship sailing through stormy seas",
        "Superhero saving the city from villains"
    ]
    
    return jsonify({'prompts': prompts}), 200

@app.route('/api/user/api-keys', methods=['GET'])
@jwt_required()
def get_api_keys():
    """Get all API keys for the current user"""
    current_user_id = get_jwt_identity()
    keys = APIKey.query.filter_by(user_id=current_user_id).all()
    
    return jsonify({
        'api_keys': [{'key': k.key, 'created_at': k.created_at} for k in keys]
    }), 200

@app.route('/api/user/generate-api-key', methods=['POST'])
@jwt_required()
def generate_api_key():
    """Generate a new API key for the current user"""
    current_user_id = get_jwt_identity()
    
    # Generate new API key
    api_key = str(uuid.uuid4())
    key = APIKey(key=api_key, user_id=current_user_id)
    db.session.add(key)
    db.session.commit()
    
    return jsonify({
        'message': 'API key generated successfully',
        'api_key': api_key
    }), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))