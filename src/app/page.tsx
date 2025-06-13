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
  SimpleGrid,
  ThemeIcon,
  useMantineColorScheme
} from '@mantine/core'
import { IconTrendingUp, IconChartLine, IconCurrencyDollar, IconBrain, IconArrowRight, IconShield, IconClock, IconUsers } from '@tabler/icons-react'

export default function Home() {
  const { colorScheme } = useMantineColorScheme()
  
  return (
    <>
      {/* Hero Section */}
      <Box 
        style={{ 
          backgroundColor: colorScheme === 'dark' ? '#000' : '#FFF',
          minHeight: '80vh',
          display: 'flex',
          alignItems: 'center'
        }}
      >
        <Container size="xl" py={80}>
          <Grid>
            <Grid.Col span={{ base: 12, md: 8 }}>
              <Stack gap="xl">
                <Title 
                  order={1} 
                  size="3.5rem"
                  fw={700}
                  lh={1.1}
                  style={{ 
                    color: colorScheme === 'dark' ? '#FFF' : '#000',
                    letterSpacing: '-0.02em'
                  }}
                >
                  Finansal piyasaları{' '}
                  <Text 
                    span 
                    style={{ 
                      color: '#FFC300',
                      background: 'linear-gradient(45deg, #FFC300, #FFD700)',
                      WebkitBackgroundClip: 'text',
                      WebkitTextFillColor: 'transparent'
                    }}
                  >
                    dönüştürün
                  </Text>
                </Title>
                
                <Text 
                  size="xl" 
                  c="dimmed" 
                  maw={600}
                  lh={1.6}
                  style={{ fontSize: '1.25rem' }}
                >
                  BIST hisse senetleri ve döviz kurları için kapsamlı analiz platformu. 
                  AI destekli öngörüler ile yatırım kararlarınızı güçlendirin.
                </Text>

                <Group gap="md" mt="xl">
                  <Button
                    size="lg"
                    radius="md"
                    rightSection={<IconArrowRight size={20} />}
                    style={{
                      backgroundColor: '#FFC300',
                      color: '#000',
                      fontWeight: 600,
                      fontSize: '1rem',
                      height: '48px',
                      paddingLeft: '2rem',
                      paddingRight: '2rem'
                    }}
                  >
                    Hemen Başlayın
                  </Button>
                  
                  <Button
                    size="lg"
                    variant="outline"
                    radius="md"
                    style={{
                      borderColor: colorScheme === 'dark' ? '#FFF' : '#000',
                      color: colorScheme === 'dark' ? '#FFF' : '#000',
                      height: '48px',
                      paddingLeft: '2rem',
                      paddingRight: '2rem'
                    }}
                  >
                                         Demo&apos;yu İzleyin
                  </Button>
                </Group>

                {/* Stats */}
                <Group gap="xl" mt="xl">
                  <div>
                    <Title order={2} mb={4} style={{ color: '#FFC300' }}>500+</Title>
                    <Text size="sm" c="dimmed">Takip Edilen Hisse</Text>
                  </div>
                  <div>
                    <Title order={2} mb={4} style={{ color: '#FFC300' }}>24/7</Title>
                    <Text size="sm" c="dimmed">Canlı Veri Akışı</Text>
                  </div>
                  <div>
                    <Title order={2} mb={4} style={{ color: '#FFC300' }}>AI</Title>
                    <Text size="sm" c="dimmed">Destekli Analiz</Text>
                  </div>
                </Group>
              </Stack>
            </Grid.Col>
            
            {/* Right side - Could add an illustration or dashboard preview */}
            <Grid.Col span={{ base: 12, md: 4 }}>
              <Box
                style={{
                  height: '400px',
                  backgroundColor: colorScheme === 'dark' ? '#111' : '#F8F9FA',
                  borderRadius: '12px',
                  border: `1px solid ${colorScheme === 'dark' ? '#333' : '#E9ECEF'}`,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center'
                }}
              >
                <Text c="dimmed">Dashboard Preview</Text>
              </Box>
            </Grid.Col>
          </Grid>
        </Container>
      </Box>

      {/* Features Section */}
      <Box 
        py={80}
        style={{ 
          backgroundColor: colorScheme === 'dark' ? '#111' : '#F8F9FA'
        }}
      >
        <Container size="xl">
          <Stack align="center" mb={60}>
            <Title 
              order={2} 
              size="2.5rem"
              fw={700}
              ta="center"
              style={{ 
                color: colorScheme === 'dark' ? '#FFF' : '#000',
                letterSpacing: '-0.02em'
              }}
            >
              Finansal verilerinizi güçlendirin
            </Title>
            <Text size="lg" c="dimmed" ta="center" maw={600}>
              Modern finansal analiz araçları ile piyasalarda öne geçin
            </Text>
          </Stack>

          <SimpleGrid cols={{ base: 1, md: 3 }} spacing="xl">
            <Card 
              shadow="sm" 
              padding="xl" 
              radius="md" 
              style={{
                backgroundColor: colorScheme === 'dark' ? '#000' : '#FFF',
                border: `1px solid ${colorScheme === 'dark' ? '#333' : '#E9ECEF'}`,
                height: '100%'
              }}
            >
              <ThemeIcon 
                size="xl" 
                radius="md"
                style={{ backgroundColor: '#FFC300', color: '#000' }}
                mb="md"
              >
                <IconChartLine size={28} />
              </ThemeIcon>
              
              <Title order={3} mb="md" style={{ color: colorScheme === 'dark' ? '#FFF' : '#000' }}>
                Hisse Senetleri
              </Title>
              <Text c="dimmed" mb="md">
                                 BIST&apos;te işlem gören tüm hisse senetlerinin anlık fiyatları, 
                teknik analiz göstergeleri ve detaylı finansal raporları.
              </Text>
              <Badge color="#FFC300" variant="light">
                500+ Hisse
              </Badge>
            </Card>

            <Card 
              shadow="sm" 
              padding="xl" 
              radius="md"
              style={{
                backgroundColor: colorScheme === 'dark' ? '#000' : '#FFF',
                border: `1px solid ${colorScheme === 'dark' ? '#333' : '#E9ECEF'}`,
                height: '100%'
              }}
            >
              <ThemeIcon 
                size="xl" 
                radius="md"
                style={{ backgroundColor: '#FFC300', color: '#000' }}
                mb="md"
              >
                <IconCurrencyDollar size={28} />
              </ThemeIcon>
              
              <Title order={3} mb="md" style={{ color: colorScheme === 'dark' ? '#FFF' : '#000' }}>
                Döviz Kurları
              </Title>
              <Text c="dimmed" mb="md">
                Başlıca döviz çiftlerinin canlı kurları, tarihsel veriler 
                ve volatilite analizleri ile kur tahminleri.
              </Text>
              <Badge color="#FFC300" variant="light">
                8 Döviz Çifti
              </Badge>
            </Card>

            <Card 
              shadow="sm" 
              padding="xl" 
              radius="md"
              style={{
                backgroundColor: colorScheme === 'dark' ? '#000' : '#FFF',
                border: `1px solid ${colorScheme === 'dark' ? '#333' : '#E9ECEF'}`,
                height: '100%'
              }}
            >
              <ThemeIcon 
                size="xl" 
                radius="md"
                style={{ backgroundColor: '#FFC300', color: '#000' }}
                mb="md"
              >
                <IconBrain size={28} />
              </ThemeIcon>
              
              <Title order={3} mb="md" style={{ color: colorScheme === 'dark' ? '#FFF' : '#000' }}>
                AI Uzman Sistemi
              </Title>
              <Text c="dimmed" mb="md">
                Makine öğrenmesi algoritmaları ile gelişmiş piyasa analizi, 
                risk değerlendirmesi ve yatırım önerileri.
              </Text>
              <Badge color="orange" variant="light">
                Yakında
              </Badge>
            </Card>
          </SimpleGrid>
        </Container>
      </Box>

      {/* Trust Section */}
      <Box py={80}>
        <Container size="xl">
          <Grid>
            <Grid.Col span={{ base: 12, md: 6 }}>
              <Stack>
                <Title 
                  order={2} 
                  size="2rem"
                  fw={700}
                  style={{ 
                    color: colorScheme === 'dark' ? '#FFF' : '#000'
                  }}
                >
                  Güvenilir finansal veriler
                </Title>
                <Text size="lg" c="dimmed" lh={1.6}>
                  Kurumsal düzeyde güvenlik ve doğruluk ile finansal verilerinizi koruyoruz. 
                  Gerçek zamanlı veri akışı ve yedekli sistemlerle kesintisiz hizmet sunuyoruz.
                </Text>
                
                <SimpleGrid cols={2} spacing="lg" mt="lg">
                  <Group>
                    <ThemeIcon size="md" style={{ backgroundColor: '#FFC300', color: '#000' }}>
                      <IconShield size={18} />
                    </ThemeIcon>
                    <div>
                      <Text fw={600} style={{ color: colorScheme === 'dark' ? '#FFF' : '#000' }}>
                        Güvenli
                      </Text>
                      <Text size="sm" c="dimmed">Bank düzeyinde güvenlik</Text>
                    </div>
                  </Group>
                  
                  <Group>
                    <ThemeIcon size="md" style={{ backgroundColor: '#FFC300', color: '#000' }}>
                      <IconClock size={18} />
                    </ThemeIcon>
                    <div>
                      <Text fw={600} style={{ color: colorScheme === 'dark' ? '#FFF' : '#000' }}>
                        Hızlı
                      </Text>
                      <Text size="sm" c="dimmed">Milisaniye yanıt süresi</Text>
                    </div>
                  </Group>
                  
                  <Group>
                    <ThemeIcon size="md" style={{ backgroundColor: '#FFC300', color: '#000' }}>
                      <IconUsers size={18} />
                    </ThemeIcon>
                    <div>
                      <Text fw={600} style={{ color: colorScheme === 'dark' ? '#FFF' : '#000' }}>
                        Destekli
                      </Text>
                      <Text size="sm" c="dimmed">7/24 teknik destek</Text>
                    </div>
                  </Group>
                  
                  <Group>
                    <ThemeIcon size="md" style={{ backgroundColor: '#FFC300', color: '#000' }}>
                      <IconTrendingUp size={18} />
                    </ThemeIcon>
                    <div>
                      <Text fw={600} style={{ color: colorScheme === 'dark' ? '#FFF' : '#000' }}>
                        Kapsamlı
                      </Text>
                      <Text size="sm" c="dimmed">Tüm piyasa verileri</Text>
                    </div>
                  </Group>
                </SimpleGrid>
              </Stack>
            </Grid.Col>
            
            <Grid.Col span={{ base: 12, md: 6 }}>
              <Box
                style={{
                  height: '300px',
                  backgroundColor: colorScheme === 'dark' ? '#111' : '#F8F9FA',
                  borderRadius: '12px',
                  border: `1px solid ${colorScheme === 'dark' ? '#333' : '#E9ECEF'}`,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center'
                }}
              >
                <Text c="dimmed">Güvenlik İllüstrasyonu</Text>
              </Box>
            </Grid.Col>
          </Grid>
        </Container>
      </Box>

      {/* CTA Section */}
      <Box 
        py={80}
        style={{ 
          backgroundColor: colorScheme === 'dark' ? '#111' : '#F8F9FA'
        }}
      >
        <Container size="md">
          <Stack align="center" ta="center">
            <Title 
              order={2} 
              size="2.5rem"
              fw={700}
              style={{ 
                color: colorScheme === 'dark' ? '#FFF' : '#000'
              }}
            >
              Finansal başarınız için hazır mısınız?
            </Title>
            <Text size="lg" c="dimmed" maw={500}>
              Bugün başlayın ve finansal verilerinizi güçlendirin. 
              Ücretsiz deneme ile tüm özellikleri keşfedin.
            </Text>
            
            <Button
              size="xl"
              radius="md"
              rightSection={<IconArrowRight size={20} />}
              style={{
                backgroundColor: '#FFC300',
                color: '#000',
                fontWeight: 600,
                fontSize: '1.125rem',
                height: '56px',
                paddingLeft: '2.5rem',
                paddingRight: '2.5rem',
                marginTop: '2rem'
              }}
            >
              Ücretsiz Başlayın
            </Button>
          </Stack>
        </Container>
      </Box>
    </>
  )
}
