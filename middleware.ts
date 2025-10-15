import { NextRequest, NextResponse } from 'next/server'

// Configuration
const PASSWORD = process.env.SITE_PASSWORD || 'Naphome2025!Secure'
const BYPASS_TOKEN = process.env.BYPASS_TOKEN || 'naphome-bypass-2025'

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl
  
  // Skip middleware for static assets
  if (
    pathname.startsWith('/_next/') ||
    pathname.startsWith('/favicon.ico') ||
    pathname.startsWith('/robots.txt') ||
    pathname.startsWith('/sitemap.xml') ||
    pathname.includes('.css') ||
    pathname.includes('.js') ||
    pathname.includes('.png') ||
    pathname.includes('.jpg') ||
    pathname.includes('.jpeg') ||
    pathname.includes('.gif') ||
    pathname.includes('.svg') ||
    pathname.includes('.ico')
  ) {
    return NextResponse.next()
  }

  // Check for bypass token in query params
  const bypassToken = request.nextUrl.searchParams.get('bypass')
  if (bypassToken === BYPASS_TOKEN) {
    return NextResponse.next()
  }

  // Check if user is already authenticated
  const isAuthenticated = request.cookies.get('naphome-auth')?.value === 'authenticated'
  
  if (isAuthenticated) {
    return NextResponse.next()
  }

  // Show auth page
  if (pathname === '/auth') {
    return NextResponse.next()
  }

  // Redirect to auth page for all other requests
  return NextResponse.redirect(new URL('/auth', request.url))
}

export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     * - public folder
     */
    '/((?!_next/static|_next/image|favicon.ico|public/).*)',
  ],
}
