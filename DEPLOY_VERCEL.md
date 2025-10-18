# Deploying GenVid to Vercel

This guide will walk you through deploying the GenVid application to Vercel.

## Prerequisites

1. Create a [Vercel account](https://vercel.com/signup)
2. Install [Vercel CLI](https://vercel.com/cli) (optional but recommended)

## Deployment Steps

### Option 1: Deploy using Vercel CLI (Recommended)

1. Install Vercel CLI globally:
   ```bash
   npm install -g vercel
   ```

2. Login to your Vercel account:
   ```bash
   vercel login
   ```

3. Navigate to your project directory and deploy:
   ```bash
   vercel
   ```

4. Follow the prompts:
   - Set up and deploy? `Y`
   - Which scope? (Select your personal account or team)
   - Link to existing project? `N`
   - What's your project's name? `genvid` (or any name you prefer)
   - In which directory is your code located? `./`
   - Want to override the settings? `N`

5. Set environment variables:
   ```bash
   vercel env add SECRET_KEY
   ```
   When prompted, enter a strong secret key for your application.

### Option 2: Deploy using Git Integration

1. Push your code to GitHub, GitLab, or Bitbucket
2. Go to [Vercel Dashboard](https://vercel.com/dashboard)
3. Click "New Project"
4. Import your Git repository
5. Configure the project:
   - Framework Preset: `Other`
   - Root Directory: `/`
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: ` `
   - Install Command: ` `
6. Add environment variables in the "Environment Variables" section:
   - `SECRET_KEY`: Your secret key (use a strong random string)

## Configuration Details

### vercel.json

The application includes a [vercel.json](file:///C:/Users/Enzo/Documents/GenVid/vercel.json) configuration that:
- Specifies Python 3.9 runtime
- Configures the build process to use the Python buildpack
- Routes all requests to your Flask application
- Sets appropriate memory limits

### Environment Variables

The application uses these environment variables:
- `SECRET_KEY`: Flask secret key for security (required)
- `DATABASE_URL`: Database connection string (optional, defaults to SQLite)

## Custom Domain (Optional)

To use a custom domain:

1. In your Vercel project dashboard, go to Settings > Domains
2. Add your custom domain
3. Follow the instructions to configure your DNS

## Scaling and Monitoring

Vercel automatically scales your application based on demand. You can monitor your application through:

1. Vercel Dashboard
2. Vercel CLI:
   ```bash
   vercel logs [your-project-name]
   ```

## Database Considerations

The application currently uses SQLite, which works for development but is not recommended for production on Vercel due to its serverless nature. For production use, consider using a managed database service like:

1. [Vercel Postgres](https://vercel.com/postgres)
2. Supabase
3. PlanetScale
4. AWS RDS
5. Google Cloud SQL

To use an external database:

1. Set the `DATABASE_URL` environment variable to your database connection string
2. Update your [models.py](file:///C:/Users/Enzo/Documents/GenVid/models.py) if needed for your specific database

## Troubleshooting

### Common Issues

1. **Build failures**: Check that all dependencies in [requirements.txt](file:///C:/Users/Enzo/Documents/GenVid/requirements.txt) are correctly specified
2. **Import errors**: Make sure all required packages are listed in requirements.txt
3. **File system issues**: Vercel's serverless functions have ephemeral file systems. Uploaded files may not persist across function invocations

### Checking Logs

View detailed logs to diagnose issues:

```bash
vercel logs [your-project-name]
```

### Health Checks

The application includes a `/health` endpoint that returns a JSON response indicating the application is running properly.

## Windows-Specific Instructions

### Installing Node.js and npm on Windows

To use the Vercel CLI on Windows:

1. Download and install Node.js from [nodejs.org](https://nodejs.org/)
2. Open a new command prompt
3. Verify installation:
   ```cmd
   node --version
   npm --version
   ```

### Using PowerShell

If you're using PowerShell, you might need to adjust execution policies:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Conclusion

Your GenVid application should now be successfully deployed to Vercel! The application is accessible via HTTPS and includes all the functionality of the local version, including user registration, video generation, and API key management.