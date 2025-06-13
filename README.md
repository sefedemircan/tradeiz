# TRIZ Trade

Modern finansal veri platformu - BIST hisse senetleri ve döviz kurları için kapsamlı analiz ve AI destekli öngörüler.

## 🚀 Özellikler

- **Real-time Veri**: BIST hisse senetleri ve döviz kurları
- **Modern UI**: Mantine UI ile responsive tasarım
- **API Backend**: FastAPI ile güçlü backend
- **Database**: Supabase PostgreSQL entegrasyonu
- **AI Analiz**: Gelişmiş finansal analiz araçları (yakında)

## 🛠️ Teknoloji Stack

### Frontend
- **Next.js 15** - React framework
- **Mantine UI** - Modern component library
- **TypeScript** - Type safety
- **Tabler Icons** - Icon set

### Backend
- **FastAPI** - Python web framework
- **Supabase** - Database ve authentication
- **yfinance** - Finansal veri kaynağı
- **Pydantic** - Data validation

## 📦 Kurulum

### 1. Hızlı Başlangıç

```bash
# Projeyi klonla
git clone <repository-url>
cd triz-trade

# Environment dosyalarını oluştur ve bağımlılıkları yükle
npm run setup

# Geliştirme sunucularını başlat
npm run dev:all
```

### 2. Manuel Kurulum

```bash
# 1. Environment dosyalarını oluştur
npm run setup:env

# 2. Frontend bağımlılıklarını yükle
npm install

# 3. Backend bağımlılıklarını yükle
npm run backend:install

# 4. Sunucuları başlat
npm run dev:all
```

## 🔧 Environment Konfigürasyonu

Proje tek bir `.env` dosyası kullanır (root dizinde). Bu dosya hem frontend hem de backend için tüm gerekli konfigürasyonları içerir.

### Tek `.env` dosyası (Frontend + Backend)
```env
# Supabase Configuration (Shared)
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_anon_key

# Frontend (Next.js) - Must use NEXT_PUBLIC_ prefix
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
NEXT_PUBLIC_API_URL=http://localhost:8000

# Backend (FastAPI)
DEBUG=true
ENVIRONMENT=development
HOST=127.0.0.1
PORT=8000

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
CORS_ORIGINS=["http://localhost:3000", "http://127.0.0.1:3000"]

# Data Collection
DATA_UPDATE_INTERVAL=300
CURRENCY_UPDATE_INTERVAL=60

# Logging
LOG_LEVEL=INFO
```

## 🚀 Kullanım

### Geliştirme Sunucuları

```bash
# Frontend + Backend birlikte
npm run dev:all

# Sadece frontend (port 3000)
npm run dev

# Sadece backend (port 8000)
npm run backend:dev
```

### Erişim URL'leri

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📱 Sayfalar

- **Ana Sayfa** (`/`) - Platform tanıtımı ve genel bilgiler
- **Hisse Senetleri** (`/stocks`) - BIST hisse senetleri listesi
- **Döviz Kurları** (`/currencies`) - Döviz kurları ve analiz
- **Uzman Sistemi** (`/expert`) - AI destekli analiz (yakında)

## 🔗 API Endpoints

### Temel Endpoints
- `GET /health` - Sistem durumu
- `GET /api/v1/info` - API bilgileri

### Hisse Senetleri
- `GET /api/v1/stocks/` - Hisse listesi
- `GET /api/v1/stocks/{id}` - Hisse detayı
- `GET /api/v1/stocks/{id}/prices` - Fiyat geçmişi
- `GET /api/v1/stocks/sectors/list` - Sektör listesi

### Döviz Kurları
- `GET /api/v1/currencies/` - Döviz listesi
- `GET /api/v1/currencies/{id}` - Döviz detayı
- `GET /api/v1/currencies/{id}/rates` - Kur geçmişi

### Veri Yönetimi
- `POST /api/v1/data/refresh/stocks` - Hisse verilerini yenile
- `POST /api/v1/data/refresh/currencies` - Döviz verilerini yenile
- `GET /api/v1/data/status` - Veri durumu

## 🗄️ Database Schema

### Tablolar
- `stocks` - Hisse senedi bilgileri
- `stock_prices` - Hisse fiyat geçmişi
- `currencies` - Döviz çiftleri
- `currency_rates` - Döviz kuru geçmişi
- `user_watchlists` - Kullanıcı takip listeleri (yakında)

## 🧪 Test

```bash
# Frontend testleri
npm run test

# Backend testleri
cd backend && python -m pytest tests/
```

## 📈 Geliştirme Roadmap

- [x] Temel frontend ve backend yapısı
- [x] Supabase entegrasyonu
- [x] Hisse senetleri ve döviz kurları sayfaları
- [ ] Real-time veri güncellemeleri
- [ ] Kullanıcı authentication sistemi
- [ ] AI destekli analiz araçları
- [ ] Grafik ve chart entegrasyonu
- [ ] Mobil uygulama
- [ ] Production deployment

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📄 Lisans

Bu proje özel bir projedir. Tüm hakları saklıdır.
