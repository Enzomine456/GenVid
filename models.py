from app import db
from datetime import datetime
import hashlib
import secrets

class User(db.Model):
    """User model for storing user information"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # In production, this should be hashed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    api_keys = db.relationship('APIKey', backref='user', lazy=True)
    video_requests = db.relationship('VideoRequest', backref='user', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'

class APIKey(db.Model):
    """API Key model for authenticating requests"""
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    def __init__(self, key=None, user_id=None):
        if key is None:
            # Generate a secure random API key
            self.key = secrets.token_urlsafe(32)
        else:
            self.key = key
        self.user_id = user_id
    
    def __repr__(self):
        return f'<APIKey {self.key[:10]}...>'

class VideoRequest(db.Model):
    """Model for storing video generation requests"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    reference_images = db.Column(db.Text, nullable=True)  # JSON list of image filenames
    status = db.Column(db.String(50), default='pending')  # pending, processing, completed, failed
    result_url = db.Column(db.String(255), nullable=True)
    request_metadata = db.Column(db.Text, nullable=True)  # Store additional data as JSON (renamed from metadata)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<VideoRequest {self.id}: {self.prompt[:50]}...>'