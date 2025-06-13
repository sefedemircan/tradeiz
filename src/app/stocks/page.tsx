'use client'

import { 
  Container, 
  Title, 
  Text, 
  Grid, 
  Card, 
  Badge,
  Group,
  Button,
  Stack,
  Box,
  Table,
  TextInput,
  Select,
  Pagination,
  Loader,
  Alert,
  ActionIcon
} from '@mantine/core'
import { IconSearch, IconRefresh, IconTrendingUp, IconAlertCircle } from '@tabler/icons-react'
import { useState } from 'react'
import { useStocks } from '../../../hooks/useApi'

export default function StocksPage() {
  const [page, setPage] = useState(1)
  const [search, setSearch] = useState('')
  const [sector, setSector] = useState<string | null>(null)
  
  const { stocks, total, loading, error } = useStocks({
    page,
    size: 20,
    search: search || undefined,
    sector: sector || undefined
  })

  const totalPages = Math.ceil(total / 20)

  const formatPrice = (price: number) => {
    return new Intl.NumberFormat('tr-TR', {
      style: 'currency',
      currency: 'TRY',
      minimumFractionDigits: 2
    }).format(price)
  }

  const formatMarketCap = (marketCap: number) => {
    if (marketCap >= 1e9) {
      return `${(marketCap / 1e9).toFixed(1)}B ₺`
    } else if (marketCap >= 1e6) {
      return `${(marketCap / 1e6).toFixed(1)}M ₺`
    }
    return `${marketCap.toLocaleString('tr-TR')} ₺`
  }

  return (
    <Container size="xl" py="xl">
      <Stack gap="xl">
        {/* Header */}
        <Box>
          <Title order={1} mb="md">Hisse Senetleri</Title>
          <Text c="dimmed" size="lg">
            BIST&apos;te işlem gören hisse senetlerinin anlık fiyatları ve detaylı analizleri
          </Text>
        </Box>

        {/* Filters */}
        <Card shadow="sm" padding="lg" radius="md">
          <Grid>
            <Grid.Col span={{ base: 12, md: 6 }}>
              <TextInput
                placeholder="Hisse adı veya sembolü ara..."
                leftSection={<IconSearch size={16} />}
                value={search}
                onChange={(event) => setSearch(event.currentTarget.value)}
              />
            </Grid.Col>
            <Grid.Col span={{ base: 12, md: 4 }}>
              <Select
                placeholder="Sektör seçin"
                data={[
                  { value: 'Bankacılık', label: 'Bankacılık' },
                  { value: 'Teknoloji', label: 'Teknoloji' },
                  { value: 'Enerji', label: 'Enerji' },
                  { value: 'Telekomünikasyon', label: 'Telekomünikasyon' },
                  { value: 'Perakende', label: 'Perakende' }
                ]}
                value={sector}
                onChange={setSector}
                clearable
              />
            </Grid.Col>
            <Grid.Col span={{ base: 12, md: 2 }}>
              <Button
                variant="light"
                leftSection={<IconRefresh size={16} />}
                onClick={() => {
                  setSearch('')
                  setSector(null)
                  setPage(1)
                }}
                fullWidth
              >
                Temizle
              </Button>
            </Grid.Col>
          </Grid>
        </Card>

        {/* Error State */}
        {error && (
          <Alert 
            icon={<IconAlertCircle size={16} />} 
            title="Hata" 
            color="red"
          >
            {error}
          </Alert>
        )}

        {/* Loading State */}
        {loading && (
          <Box ta="center" py="xl">
            <Loader size="lg" />
            <Text mt="md" c="dimmed">Hisse senetleri yükleniyor...</Text>
          </Box>
        )}

        {/* Stocks Table */}
        {!loading && !error && (
          <Card shadow="sm" padding="lg" radius="md">
            <Group justify="space-between" mb="md">
              <Title order={3}>Hisse Senetleri ({total})</Title>
              <ActionIcon variant="light" size="lg">
                <IconRefresh size={16} />
              </ActionIcon>
            </Group>

            {stocks.length === 0 ? (
              <Box ta="center" py="xl">
                <Text c="dimmed">Hiç hisse senedi bulunamadı.</Text>
              </Box>
            ) : (
              <>
                <Table striped highlightOnHover>
                  <Table.Thead>
                    <Table.Tr>
                      <Table.Th>Sembol</Table.Th>
                      <Table.Th>Şirket Adı</Table.Th>
                      <Table.Th>Sektör</Table.Th>
                      <Table.Th>Piyasa Değeri</Table.Th>
                      <Table.Th>Durum</Table.Th>
                    </Table.Tr>
                  </Table.Thead>
                  <Table.Tbody>
                    {stocks.map((stock) => (
                      <Table.Tr key={stock.id}>
                        <Table.Td>
                          <Text fw={600} c="blue">
                            {stock.symbol}
                          </Text>
                        </Table.Td>
                        <Table.Td>
                          <Text>{stock.name}</Text>
                        </Table.Td>
                        <Table.Td>
                          <Badge variant="light" size="sm">
                            {stock.sector}
                          </Badge>
                        </Table.Td>
                        <Table.Td>
                          <Text>
                            {stock.market_cap ? formatMarketCap(stock.market_cap) : 'N/A'}
                          </Text>
                        </Table.Td>
                        <Table.Td>
                          <Badge 
                            color="green" 
                            variant="light"
                            leftSection={<IconTrendingUp size={12} />}
                          >
                            Aktif
                          </Badge>
                        </Table.Td>
                      </Table.Tr>
                    ))}
                  </Table.Tbody>
                </Table>

                {/* Pagination */}
                {totalPages > 1 && (
                  <Group justify="center" mt="xl">
                    <Pagination
                      value={page}
                      onChange={setPage}
                      total={totalPages}
                      size="md"
                    />
                  </Group>
                )}
              </>
            )}
          </Card>
        )}

        {/* Summary Stats */}
        {!loading && !error && stocks.length > 0 && (
          <Grid>
            <Grid.Col span={{ base: 12, md: 4 }}>
              <Card shadow="sm" padding="lg" radius="md" ta="center">
                <Title order={2} c="green">{stocks.length}</Title>
                <Text c="dimmed">Bu Sayfada</Text>
              </Card>
            </Grid.Col>
            <Grid.Col span={{ base: 12, md: 4 }}>
              <Card shadow="sm" padding="lg" radius="md" ta="center">
                <Title order={2} c="blue">{total}</Title>
                <Text c="dimmed">Toplam Hisse</Text>
              </Card>
            </Grid.Col>
            <Grid.Col span={{ base: 12, md: 4 }}>
              <Card shadow="sm" padding="lg" radius="md" ta="center">
                <Title order={2} c="orange">{new Set(stocks.map(s => s.sector)).size}</Title>
                <Text c="dimmed">Farklı Sektör</Text>
              </Card>
            </Grid.Col>
          </Grid>
        )}
      </Stack>
    </Container>
  )
} 