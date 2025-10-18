# Deploying GenVid to Fly.io

This guide will walk you through deploying the GenVid application to Fly.io.

## Prerequisites

1. Install [Fly.io CLI](https://fly.io/docs/getting-started/installing-flyctl/)
2. Create a [Fly.io account](https://fly.io/app/sign-up)

## Deployment Steps

### 1. Login to Fly.io

```bash
flyctl auth login
```

### 2. Launch Your App

Navigate to your project directory and launch the app:

```bash
flyctl launch
```

Follow the prompts:
- Choose a unique app name
- Select a region closest to your users
- When asked if you would like to set up a Postgresql database, type "No" for now (we'll use SQLite for simplicity)
- When asked if you would like to set up Redis, type "No"
- When asked if you would like to deploy now, type "No"

### 3. Set Environment Variables

Set the secret key for your application:

```bash
flyctl secrets set SECRET_KEY="your-super-secret-key-here"
```

For production, use a strong random key. You can generate one with:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 4. Deploy the Application

Deploy your application to Fly.io:

```bash
flyctl deploy
```

### 5. Open Your Application

Once deployed, open your application in the browser:

```bash
flyctl open
```

## Configuration Details

### Dockerfile

The application includes a [Dockerfile](file:///C:/Users/Enzo/Documents/GenVid/Dockerfile) that:
- Uses Python 3.9 slim image
- Installs system dependencies including ffmpeg
- Installs Python requirements
- Exposes port 8080
- Runs the application with Gunicorn

### fly.toml

The [fly.toml](file:///C:/Users/Enzo/Documents/GenVid/fly.toml) configuration:
- Sets the internal port to 8080
- Configures HTTPS enforcement
- Enables auto start/stop of machines
- Uses the Dockerfile for building

### Environment Variables

The application uses these environment variables:
- `SECRET_KEY`: Flask secret key for security
- `PORT`: Port to run the application on (set by Fly.io)
- `DATABASE_URL`: Database connection string (defaults to SQLite)

## Scaling and Monitoring

### View Application Status

```bash
flyctl status
```

### View Application Logs

```bash
flyctl logs
```

### Scale to Multiple Instances

```bash
flyctl scale count 2
```

## Using a Persistent Database (Optional)

For production use, you might want to use a persistent database instead of SQLite.

### Create a Postgresql Database

```bash
flyctl postgres create
```

Follow the prompts to create a database cluster.

### Attach the Database to Your App

```bash
flyctl postgres attach YOUR_DATABASE_NAME
```

This will set the `DATABASE_URL` environment variable for your application.

## Troubleshooting

### Common Issues

1. **Build failures**: Check that all dependencies in [requirements.txt](file:///C:/Users/Enzo/Documents/GenVid/requirements.txt) are correctly specified
2. **Deployment timeouts**: If your app takes too long to start, increase the timeout in fly.toml
3. **Memory issues**: Scale your app to a larger VM size with `flyctl scale vm shared-cpu-2x`

### Checking Logs

View detailed logs to diagnose issues:

```bash
flyctl logs
```

### Health Checks

The application includes a `/health` endpoint that returns a JSON response indicating the application is running properly.

## Windows-Specific Instructions

### Installing Flyctl on Windows

On Windows, you can install Flyctl using Winget:

```cmd
winget install flyctl
```

### PATH Issues on Windows

After installing flyctl on Windows, you need to restart your command prompt for the PATH changes to take effect. If you get an error like "'fly' is not recognized as an internal or external command", close your current command prompt and open a new one.

### Using the Windows Deployment Helper

This project includes a Windows deployment helper script ([deploy_windows.bat](file:///C:/Users/Enzo/Documents/GenVid/deploy_windows.bat)) that can help you with the deployment process:

1. Double-click on `deploy_windows.bat` or run it from the command line:
   ```cmd
   deploy_windows.bat
   ```

2. The script will:
   - Check if flyctl is properly installed
   - Run the fix script
   - Provide guidance for the deployment process

## Custom Domain (Optional)

To use a custom domain:

1. Add your domain to Fly.io:
   ```bash
   flyctl certs add yourdomain.com
   ```

2. Configure your DNS to point to the Fly.io DNS targets provided in the output.

## Conclusion

Your GenVid application should now be successfully deployed to Fly.io! The application is accessible via HTTPS and includes all the functionality of the local version, including user registration, video generation, and API key management.