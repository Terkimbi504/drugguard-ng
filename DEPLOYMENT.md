# Deployment Guide for DrugGuard NG
clear

## Frontend Deployment (React + Vite)

### Option 1: Deploy to Vercel (Recommended)

#### Step 1: Create Vercel Account
1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub account

#### Step 2: Deploy
```bash
cd frontend
npm run build  # Creates optimized build
```

Then use Vercel CLI or connect GitHub repo to Vercel dashboard.

#### Step 3: Configure Environment
In Vercel dashboard:
```
Environment Variables:
VITE_API_URL=https://your-backend-domain.com
```

Update `frontend/src/services/api.js`:
```javascript
const API_BASE_URL = import.meta.env.VITE_API_URL || '/api';
```

### Option 2: Deploy to Netlify

```bash
cd frontend
npm run build
```

1. Go to [netlify.com](https://netlify.com)
2. Drag and drop `dist` folder
3. Configure `_redirects` file for React Router:

Create `frontend/public/_redirects`:
```
/*    /index.html   200
```

### Option 3: Deploy to GitHub Pages

```bash
npm install --save-dev gh-pages
```

Add to `package.json`:
```json
"homepage": "https://yourusername.github.io/drugguard-ng",
"deploy": "npm run build && gh-pages -d dist"
```

Then run:
```bash
npm run deploy
```

---

## Backend Deployment (FastAPI + Python)

### Option 1: Deploy to Render (Easiest)

#### Step 1: Prepare Backend
Create `Procfile` in project root:
```
web: cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Create `render.yaml`:
```yaml
services:
  - type: web
    name: drugguard-ng-api
    runtime: python
    plan: free
    pythonVersion: 3.11
    buildCommand: pip install -r backend/requirements.txt
    startCommand: cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: FRONTEND_URL
        value: https://your-frontend-domain.com
      - key: ENVIRONMENT
        value: production
      - key: DEBUG
        value: false
```

#### Step 2: Deploy
1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Create new Web Service
4. Connect GitHub repo
5. Render automatically deploys

### Option 2: Deploy to Railway

1. Install Railway CLI: `npm i -g @railway/cli`
2. Login: `railway login`
3. Initialize: `railway init`
4. Add environment variables:
   ```bash
   railway variables set FRONTEND_URL=https://your-frontend.vercel.app
   railway variables set ENVIRONMENT=production
   ```
5. Deploy: `railway up`

### Option 3: Deploy to Heroku (Free tier deprecated, but still works)

```bash
heroku login
heroku create your-app-name
git push heroku main
heroku config:set FRONTEND_URL=https://your-frontend.com
```

### Option 4: Deploy with Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Then deploy to any Docker hosting (AWS, GCP, Azure, etc.)

---

## Database Setup for Production

### SQLite (Current Setup)
- Works out of the box
- Good for small to medium apps
- Data stored in `backend/app/drugguard.db`

**Backup your database:**
```bash
cp backend/app/drugguard.db backup_$(date +%Y%m%d_%H%M%S).db
```

### PostgreSQL (For Larger Scale)

Update `backend/app/config.py`:
```python
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://user:password@localhost/drugguard"
)
```

Install PostgreSQL driver:
```bash
pip install psycopg2-binary
```

Deploy PostgreSQL:
- Render: Integrated database option
- Railway: Add PostgreSQL service
- Heroku: Heroku Postgres add-on
- AWS RDS: Managed PostgreSQL
- DigitalOcean: Managed Database

---

## Environment Configuration

### Production Environment Variables

Create `.env` file (do NOT commit):
```env
# Backend
DATABASE_URL=postgresql://user:password@db-host/drugguard
FRONTEND_URL=https://your-frontend-domain.com
BACKEND_URL=https://your-backend-domain.com
ENVIRONMENT=production
DEBUG=false

# Optional: CORS settings
ALLOWED_ORIGINS=https://your-frontend-domain.com,https://www.your-frontend-domain.com
```

### Set in Deployment Platform

**Render:**
Go to Settings → Environment → Add variables

**Railway:**
```bash
railway variables set KEY=value
```

**Vercel:**
Go to Settings → Environment Variables

**Netlify:**
Build & Deploy → Environment → Add variables

---

## Security Checklist

Before deploying to production:

- [ ] Set `DEBUG=false`
- [ ] Change default database location
- [ ] Set secure CORS origins (not `*`)
- [ ] Enable HTTPS/SSL
- [ ] Set strong environment variable secrets
- [ ] Add input validation
- [ ] Add rate limiting
- [ ] Don't commit secrets to Git
- [ ] Use `.env.example` for documentation
- [ ] Enable CSRF protection if needed
- [ ] Set secure password policies (if adding auth)

---

## Domain Configuration

### Frontend Domain
1. Buy domain (GoDaddy, Namecheap, etc.)
2. Point to hosting platform:
   - Vercel: Add custom domain in Settings
   - Netlify: DNS settings
   - GitHub Pages: CNAME file

### Backend Domain
1. Buy domain or subdomain (e.g., api.your-domain.com)
2. Point to backend hosting:
   - Render: Add custom domain
   - Railway: Add custom domain
   - Heroku: Heroku Domains add-on

### Update Frontend
In `frontend/src/services/api.js`:
```javascript
const API_BASE_URL = 'https://api.your-domain.com';
```

---

## SSL/HTTPS

Most platforms handle this automatically:
- ✅ Vercel: Automatic SSL
- ✅ Netlify: Automatic SSL
- ✅ Render: Automatic SSL
- ✅ Railway: Automatic SSL
- ✅ Heroku: Free SSL

---

## Monitoring & Logs

### Render Dashboard
- Real-time logs
- Automatic error alerts
- Performance metrics

### Railway Dashboard
- Live logs
- Deployment history
- Resource usage

### Error Tracking (Optional)
Add to `backend/app/main.py`:
```python
from sentry_sdk.integrations.fastapi import FastApiIntegration
import sentry_sdk

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FastApiIntegration()],
    environment="production",
    traces_sample_rate=0.1
)
```

---

## Performance Optimization

### Frontend
```bash
# Build optimized bundle
npm run build

# Analyze bundle size
npm install -D vite-plugin-visualizer
```

### Backend
- Enable database indexing
- Add caching (Redis)
- Use connection pooling
- Monitor query performance

---

## Scaling Considerations

### For Larger Traffic
1. **Database**: Switch to PostgreSQL/MySQL
2. **Caching**: Add Redis for frequently accessed data
3. **API Optimization**: Add pagination, filtering
4. **Frontend**: Implement lazy loading, code splitting
5. **Infrastructure**: Auto-scaling, load balancers

---

## Troubleshooting Deployment

### Frontend Won't Load
- Check browser console (F12)
- Verify API URL is correct
- Check CORS settings in backend
- Verify backend is running

### Backend Returns 502/503
- Check platform logs
- Verify dependencies installed
- Check database connection
- Restart service

### API Calls Fail
- Check CORS settings
- Verify authentication (if added)
- Check API endpoint paths
- Verify environment variables

### Database Issues
- Backup database
- Check database connection string
- Verify database permissions
- Migrate if changing database type

---

## Continuous Deployment

### Automatic Updates on Push

**Render:**
1. Connect GitHub repo
2. Automatic deploys on push to main

**Vercel:**
1. Install Vercel app
2. Auto-deploys on GitHub push

**Railway:**
1. Connect GitHub repo
2. Deploy on push

**Heroku:**
```bash
# Connect GitHub in Heroku dashboard
# Enable "Auto Deploy"
```

---

## Cost Estimation

### Free Tier Options
- **Frontend**: Vercel Free (perfect)
- **Backend**: Render Free (includes 0.5 CPU, 512MB RAM)
- **Database**: PostgreSQL free tier on Render/Railway

### Estimated Monthly Costs (Production)
- Frontend (Vercel Pro): $20/month
- Backend (Render Starter): $7-12/month  
- Database (PostgreSQL): $15-25/month
- Domain: ~$12/year

**Total: ~$40-50/month for production**

---

## Rollback Plan

### If Deployment Goes Wrong

1. **Revert to Previous Commit**
   ```bash
   git revert HEAD
   git push
   # Platform auto-redeploys
   ```

2. **Database Rollback**
   ```bash
   # Restore from backup
   cp backup_database.db drugguard.db
   # or restore from database backup
   ```

3. **DNS Rollback**
   - Point domain back to previous IP
   - Update environment variables

---

## Support & Resources

- **Render Docs**: https://render.com/docs
- **Railway Docs**: https://railway.app/docs
- **Vercel Docs**: https://vercel.com/docs
- **FastAPI Deployment**: https://fastapi.tiangolo.com/deployment/
- **React Deployment**: https://create-react-app.dev/deployment/

---

**Congratulations on deploying DrugGuard NG!** 🎉
