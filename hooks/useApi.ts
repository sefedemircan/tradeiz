/**
 * Custom hooks for API data fetching
 */

import { useState, useEffect } from 'react';
import { apiClient, Stock, Currency } from '../lib/api';

export function useApiHealth() {
  const [health, setHealth] = useState<{ status: string; service: string; version: string } | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchHealth() {
      try {
        setLoading(true);
        const response = await apiClient.getHealth();
        
        if (response.error) {
          setError(response.error);
        } else {
          setHealth(response.data || null);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to fetch health status');
      } finally {
        setLoading(false);
      }
    }

    fetchHealth();
  }, []);

  return { health, loading, error };
}

export function useStocks(params?: {
  page?: number;
  size?: number;
  search?: string;
  sector?: string;
}) {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchStocks() {
      try {
        setLoading(true);
        const response = await apiClient.getStocks(params);
        
        if (response.error) {
          setError(response.error);
        } else if (response.data) {
          setStocks(response.data.stocks);
          setTotal(response.data.total);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to fetch stocks');
      } finally {
        setLoading(false);
      }
    }

    fetchStocks();
  }, [params?.page, params?.size, params?.search, params?.sector]);

  return { stocks, total, loading, error };
}

export function useCurrencies(params?: {
  page?: number;
  size?: number;
  search?: string;
}) {
  const [currencies, setCurrencies] = useState<Currency[]>([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchCurrencies() {
      try {
        setLoading(true);
        const response = await apiClient.getCurrencies(params);
        
        if (response.error) {
          setError(response.error);
        } else if (response.data) {
          setCurrencies(response.data.currencies);
          setTotal(response.data.total);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to fetch currencies');
      } finally {
        setLoading(false);
      }
    }

    fetchCurrencies();
  }, [params?.page, params?.size, params?.search]);

  return { currencies, total, loading, error };
}

export function useDataStatus() {
  const [status, setStatus] = useState<{
    status: string;
    last_update: string;
    stocks_count: number;
    currencies_count: number;
    data_sources: string[];
  } | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchStatus() {
      try {
        setLoading(true);
        const response = await apiClient.getDataStatus();
        
        if (response.error) {
          setError(response.error);
        } else {
          setStatus(response.data || null);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to fetch data status');
      } finally {
        setLoading(false);
      }
    }

    fetchStatus();
  }, []);

  const refresh = async () => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await apiClient.getDataStatus();
      
      if (response.error) {
        setError(response.error);
      } else {
        setStatus(response.data || null);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to refresh data status');
    } finally {
      setLoading(false);
    }
  };

  return { status, loading, error, refresh };
} 