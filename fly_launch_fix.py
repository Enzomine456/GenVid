#!/usr/bin/env python3
"""
Script to fix Fly.io launch manifest issues
"""

import os
import json
import subprocess
import sys
import platform

def fix_fly_toml():
    """Fix common issues in fly.toml"""
    fly_toml_path = "fly.toml"
    
    if not os.path.exists(fly_toml_path):
        print("fly.toml not found!")
        return False
    
    # Read the current fly.toml
    with open(fly_toml_path, 'r') as f:
        content = f.read()
    
    # Ensure the app name is consistent
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Fix any app name inconsistencies
        if line.startswith('app ='):
            # Extract app name
            app_name = line.split('=')[1].strip().strip('"')
            fixed_lines.append(f'app = "{app_name}"')
        else:
            fixed_lines.append(line)
    
    # Add deploy section if missing
    if '[deploy]' not in content:
        fixed_lines.append('')
        fixed_lines.append('[deploy]')
        fixed_lines.append('  release_command = "echo \'Deploying GenVid application\'"')
    
    # Write the fixed content back
    with open(fly_toml_path, 'w') as f:
        f.write('\n'.join(fixed_lines))
    
    print("✓ Fixed fly.toml")
    return True

def check_dockerfile():
    """Check if Dockerfile has proper configuration"""
    dockerfile_path = "Dockerfile"
    
    if not os.path.exists(dockerfile_path):
        print("Dockerfile not found!")
        return False
    
    with open(dockerfile_path, 'r') as f:
        content = f.read()
    
    # Check if PORT is set in environment variables
    if 'ENV PORT' not in content:
        lines = content.split('\n')
        # Insert PORT environment variable after other ENV declarations
        new_lines = []
        port_added = False
        
        for line in lines:
            new_lines.append(line)
            if line.startswith('ENV') and not port_added:
                new_lines.append('ENV PORT 8080')
                port_added = True
        
        with open(dockerfile_path, 'w') as f:
            f.write('\n'.join(new_lines))
        
        print("✓ Added PORT environment variable to Dockerfile")
    
    # Check if CMD uses the correct format
    if 'gunicorn' in content and 'app:app' in content:
        print("✓ Dockerfile CMD looks correct")
        return True
    
    return True

def reset_fly_manifest():
    """Reset Fly.io manifest by removing temporary files"""
    temp_files = [
        '.fly',
        '.fly/bin',
        '/tmp/manifest.json'
    ]
    
    for file_path in temp_files:
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                if platform.system() == "Windows":
                    subprocess.run(['rmdir', '/s', '/q', file_path], shell=True)
                else:
                    subprocess.run(['rm', '-rf', file_path])
            else:
                os.remove(file_path)
            print(f"Removed {file_path}")
    
    return True

def print_windows_instructions():
    """Print specific instructions for Windows users"""
    if platform.system() == "Windows":
        print("\n" + "="*60)
        print("WINDOWS-SPECIFIC INSTRUCTIONS:")
        print("="*60)
        print("1. Close this command prompt and open a NEW one")
        print("   (This refreshes the PATH environment variable)")
        print("2. After opening the new command prompt, test with:")
        print("   fly version")
        print("   OR")
        print("   flyctl version")
        print("3. Then you can deploy with:")
        print("   fly deploy")
        print("="*60)

def main():
    """Main function to fix Fly.io launch issues"""
    print("Fixing Fly.io launch manifest issues...\n")
    
    # Fix fly.toml
    if not fix_fly_toml():
        print("✗ Failed to fix fly.toml")
        sys.exit(1)
    
    # Check Dockerfile
    if not check_dockerfile():
        print("✗ Failed to check Dockerfile")
        sys.exit(1)
    
    # Reset manifest files
    reset_fly_manifest()
    
    print("\n" + "="*50)
    print("✓ All fixes applied!")
    print("You can now try running: fly deploy")
    print("Or if you still get the manifest error, try: fly launch --force")
    
    print_windows_instructions()

if __name__ == "__main__":
    main()