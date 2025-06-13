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
  Pagination,
  Loader,
  Alert,
  ActionIcon
} from '@mantine/core'
import { IconSearch, IconRefresh, IconTrendingUp, IconAlertCircle } from '@tabler/icons-react'
import { useState } from 'react'
import { useCurrencies } from '../../../hooks/useApi'

export default function CurrenciesPage() {
  const [page, setPage] = useState(1)
  const [search, setSearch] = useState('')
  
  const { currencies, total, loading, error } = useCurrencies({
    page,
    size: 20,
    search: search || undefined
  })

  const totalPages = Math.ceil(total / 20)

  const formatRate = (rate: number) => {
    return new Intl.NumberFormat('tr-TR', {
      minimumFractionDigits: 4,
      maximumFractionDigits: 4
    }).format(rate)
  }

  return (
    <Container size="xl" py="xl">
      <Stack gap="xl">
        {/* Header */}
        <Box>
          <Title order={1} mb="md">Döviz Kurları</Title>
          <Text c="dimmed" size="lg">
            Anlık döviz kurları ve detaylı kur analizleri
          </Text>
        </Box>

        {/* Filters */}
        <Card shadow="sm" padding="lg" radius="md">
          <Grid>
            <Grid.Col span={{ base: 12, md: 8 }}>
              <TextInput
                placeholder="Döviz çifti ara (örn: USD/TRY)..."
                leftSection={<IconSearch size={16} />}
                value={search}
                onChange={(event) => setSearch(event.currentTarget.value)}
              />
            </Grid.Col>
            <Grid.Col span={{ base: 12, md: 4 }}>
              <Button
                variant="light"
                leftSection={<IconRefresh size={16} />}
                onClick={() => {
                  setSearch('')
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
            <Text mt="md" c="dimmed">Döviz kurları yükleniyor...</Text>
          </Box>
        )}

        {/* Currencies Table */}
        {!loading && !error && (
          <Card shadow="sm" padding="lg" radius="md">
            <Group justify="space-between" mb="md">
              <Title order={3}>Döviz Kurları ({total})</Title>
              <ActionIcon variant="light" size="lg">
                <IconRefresh size={16} />
              </ActionIcon>
            </Group>

            {currencies.length === 0 ? (
              <Box ta="center" py="xl">
                <Text c="dimmed">Hiç döviz kuru bulunamadı.</Text>
              </Box>
            ) : (
              <>
                <Table striped highlightOnHover>
                  <Table.Thead>
                    <Table.Tr>
                      <Table.Th>Sembol</Table.Th>
                      <Table.Th>Döviz Çifti</Table.Th>
                      <Table.Th>Güncel Kur</Table.Th>
                      <Table.Th>Değişim</Table.Th>
                      <Table.Th>Durum</Table.Th>
                    </Table.Tr>
                  </Table.Thead>
                  <Table.Tbody>
                    {currencies.map((currency) => (
                      <Table.Tr key={currency.id}>
                        <Table.Td>
                          <Text fw={600} c="blue">
                            {currency.symbol}
                          </Text>
                        </Table.Td>
                        <Table.Td>
                          <Text>{currency.name}</Text>
                        </Table.Td>
                        <Table.Td>
                          <Text fw={500}>
                            {/* Placeholder rate - will be replaced with real data */}
                            {formatRate(25.50)} ₺
                          </Text>
                        </Table.Td>
                        <Table.Td>
                          <Badge 
                            color="green" 
                            variant="light"
                            leftSection={<IconTrendingUp size={12} />}
                          >
                            +1.25%
                          </Badge>
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
        {!loading && !error && currencies.length > 0 && (
          <Grid>
            <Grid.Col span={{ base: 12, md: 4 }}>
              <Card shadow="sm" padding="lg" radius="md" ta="center">
                <Title order={2} c="green">{currencies.length}</Title>
                <Text c="dimmed">Bu Sayfada</Text>
              </Card>
            </Grid.Col>
            <Grid.Col span={{ base: 12, md: 4 }}>
              <Card shadow="sm" padding="lg" radius="md" ta="center">
                <Title order={2} c="blue">{total}</Title>
                <Text c="dimmed">Toplam Döviz</Text>
              </Card>
            </Grid.Col>
            <Grid.Col span={{ base: 12, md: 4 }}>
              <Card shadow="sm" padding="lg" radius="md" ta="center">
                <Title order={2} c="orange">8</Title>
                <Text c="dimmed">Ana Dövizler</Text>
              </Card>
            </Grid.Col>
          </Grid>
        )}

        {/* Popular Currency Pairs */}
        <Card shadow="sm" padding="lg" radius="md">
          <Title order={3} mb="md">Popüler Döviz Çiftleri</Title>
          <Grid>
            {['USD/TRY', 'EUR/TRY', 'GBP/TRY', 'JPY/TRY'].map((pair) => (
              <Grid.Col key={pair} span={{ base: 12, sm: 6, md: 3 }}>
                <Card shadow="xs" padding="md" radius="md" style={{ border: '1px solid #E9ECEF' }}>
                  <Group justify="space-between" mb="xs">
                    <Text fw={600}>{pair}</Text>
                    <Badge color="green" size="sm">+1.2%</Badge>
                  </Group>
                  <Text size="lg" fw={700} c="blue">
                    {formatRate(25.50)} ₺
                  </Text>
                  <Text size="xs" c="dimmed">Son güncelleme: 2 dk önce</Text>
                </Card>
              </Grid.Col>
            ))}
          </Grid>
        </Card>
      </Stack>
    </Container>
  )
} 