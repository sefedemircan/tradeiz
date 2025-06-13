// Hisse Senedi Tipi
export interface Stock {
  id: string
  symbol: string
  name: string
  sector: string
  price: number
  change: number
  changePercent: number
  volume: number
  marketCap?: number
  lastUpdate: Date
}

// Döviz Tipi
export interface Currency {
  id: string
  symbol: string
  name: string
  rate: number
  change: number
  changePercent: number
  lastUpdate: Date
}

// Fiyat Geçmişi
export interface PriceHistory {
  id: string
  stockId?: string
  currencyId?: string
  price: number
  volume?: number
  timestamp: Date
}

// Kullanıcı Watchlist
export interface UserWatchlist {
  id: string
  userId: string
  stockId?: string
  currencyId?: string
  createdAt: Date
}

// API Response Types
export interface ApiResponse<T> {
  data: T
  success: boolean
  message?: string
  error?: string
}

// Chart Data
export interface ChartDataPoint {
  time: string
  value: number
  volume?: number
} 