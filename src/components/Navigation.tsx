'use client'

import { 
  AppShell,
  Burger, 
  Group, 
  Title,
  Button,
  ActionIcon,
  useMantineColorScheme,
  Container,
  Box
} from '@mantine/core'
import { useDisclosure } from '@mantine/hooks'
import { IconSun, IconMoon, IconChartLine, IconCurrencyDollar, IconBrain } from '@tabler/icons-react'
import Link from 'next/link'
import { usePathname } from 'next/navigation'

interface NavigationProps {
  children: React.ReactNode
}

export function Navigation({ children }: NavigationProps) {
  const [opened, { toggle }] = useDisclosure()
  const { colorScheme, toggleColorScheme } = useMantineColorScheme()
  const pathname = usePathname()

  const navItems = [
    {
      href: '/',
      label: 'Ana Sayfa',
      icon: IconChartLine
    },
    {
      href: '/stocks',
      label: 'Hisse Senetleri',
      icon: IconChartLine
    },
    {
      href: '/currencies',
      label: 'Döviz Kurları',
      icon: IconCurrencyDollar
    },
    {
      href: '/expert',
      label: 'Uzman Sistemi',
      icon: IconBrain
    }
  ]

  return (
    <AppShell
      header={{ height: 70 }}
      navbar={{
        width: 300,
        breakpoint: 'md',
        collapsed: { desktop: true, mobile: !opened }
      }}
      padding={0}
    >
      <AppShell.Header 
        style={{ 
          backgroundColor: colorScheme === 'dark' ? '#000' : '#FFF',
          borderBottom: `1px solid ${colorScheme === 'dark' ? '#333' : '#E9ECEF'}`
        }}
      >
        <Container size="xl" h="100%">
          <Group h="100%" justify="space-between">
            {/* Logo */}
            <Group>
              <Burger 
                opened={opened} 
                onClick={toggle} 
                hiddenFrom="md" 
                size="sm"
                color={colorScheme === 'dark' ? '#FFF' : '#000'}
              />
              <Link href="/" style={{ textDecoration: 'none' }}>
                <Title 
                  order={2} 
                  style={{ 
                    color: colorScheme === 'dark' ? '#FFF' : '#000',
                    fontWeight: 700,
                    letterSpacing: '-0.02em'
                  }}
                >
                  TRIZ Trade
                </Title>
              </Link>
            </Group>

            {/* Desktop Navigation */}
            <Group gap="lg" visibleFrom="md">
              {navItems.map((item) => (
                <Button
                  key={item.href}
                  component={Link}
                  href={item.href}
                  variant={pathname === item.href ? "filled" : "subtle"}
                  color={pathname === item.href ? "#FFC300" : "gray"}
                  size="sm"
                  radius="md"
                  style={{
                    color: pathname === item.href 
                      ? '#000' 
                      : colorScheme === 'dark' ? '#FFF' : '#000',
                    backgroundColor: pathname === item.href 
                      ? '#FFC300' 
                      : 'transparent',
                    fontWeight: pathname === item.href ? 600 : 500
                  }}
                >
                  {item.label}
                </Button>
              ))}
            </Group>

            {/* Actions */}
            <Group gap="md">
              <ActionIcon 
                variant="subtle" 
                size="lg"
                onClick={() => toggleColorScheme()}
                aria-label="Tema değiştir"
                style={{
                  color: colorScheme === 'dark' ? '#FFF' : '#000'
                }}
              >
                {colorScheme === 'dark' ? <IconSun size={20} /> : <IconMoon size={20} />}
              </ActionIcon>
              
              <Button
                variant="filled"
                size="sm"
                radius="md"
                style={{
                  backgroundColor: '#FFC300',
                  color: '#000',
                  fontWeight: 600,
                  border: 'none'
                }}
                visibleFrom="md"
              >
                Platformu Keşfet
              </Button>
            </Group>
          </Group>
        </Container>
      </AppShell.Header>

      {/* Mobile Navigation */}
      <AppShell.Navbar 
        p="md"
        style={{ 
          backgroundColor: colorScheme === 'dark' ? '#000' : '#FFF',
          borderRight: `1px solid ${colorScheme === 'dark' ? '#333' : '#E9ECEF'}`
        }}
      >
        <Box>
          {navItems.map((item) => (
            <Button
              key={item.href}
              component={Link}
              href={item.href}
              variant={pathname === item.href ? "filled" : "subtle"}
              leftSection={<item.icon size={18} />}
              fullWidth
              justify="flex-start"
              mb="xs"
              radius="md"
              style={{
                color: pathname === item.href 
                  ? '#000' 
                  : colorScheme === 'dark' ? '#FFF' : '#000',
                backgroundColor: pathname === item.href 
                  ? '#FFC300' 
                  : 'transparent',
                fontWeight: pathname === item.href ? 600 : 500
              }}
            >
              {item.label}
            </Button>
          ))}
        </Box>
      </AppShell.Navbar>

      <AppShell.Main>
        {children}
      </AppShell.Main>
    </AppShell>
  )
} 