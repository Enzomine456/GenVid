# Deploying to Vercel

## Prerequisites

1. Create a [Vercel account](https://vercel.com/signup)
2. Install [Vercel CLI](https://vercel.com/cli):
   ```bash
   npm install -g vercel
   ```

## Deploy Steps

1. Login to Vercel:
   ```bash
   vercel login
   ```

2. Deploy the project:
   ```bash
   vercel
   ```

3. Set the SECRET_KEY environment variable:
   ```bash
   vercel env add SECRET_KEY
   ```

## Notes

- The application uses SQLite by default, which works for development but is not recommended for production.
- For production, consider using a managed database service and set the DATABASE_URL environment variable.