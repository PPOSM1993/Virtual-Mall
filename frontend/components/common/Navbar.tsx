"use client";

import Link from "next/link";
import {
  Menu,
  Home,
  Building2,
  LayoutGrid,
  Store,
  Phone,
  Clock,
} from "lucide-react";

import Logo from "@/components/common/Logo";

import { Button } from "@/components/ui/button";
import {
  Sheet,
  SheetContent,
  SheetTrigger,
} from "@/components/ui/sheet";

const links = [
  {
    title: "Inicio",
    href: "/",
    icon: Home,
  },
  {
    title: "Empresas",
    href: "/companies",
    icon: Building2,
  },
  {
    title: "Categorías",
    href: "/categories",
    icon: LayoutGrid,
  },
  {
    title: "Booths",
    href: "/booths",
    icon: Store,
  },
    {
    title: "Horarios",
    href: "/schedules",
    icon: Clock,
  },
  {
    title: "Contacto",
    href: "/contact",
    icon: Phone,
  },
];

export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b bg-background/90 backdrop-blur-md">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6">

        <Logo />

        {/* Desktop */}
        <nav className="hidden items-center gap-8 lg:flex">
          {links.map((link) => (
            <Link
              key={link.title}
              href={link.href}
              className="text-sm font-medium transition-colors hover:text-primary"
            >
              {link.title}
            </Link>
          ))}
        </nav>

        {/* Mobile */}
        <div className="lg:hidden">
          <Sheet>
            <SheetTrigger asChild>
              <Button variant="ghost" size="icon">
                <Menu className="h-6 w-6" />
              </Button>
            </SheetTrigger>

            <SheetContent side="right" className="w-80 p-0">

              <div className="flex h-full flex-col">

                {/* Header */}
                <div className="border-b p-6">
                  <Logo />
                </div>

                {/* Navigation */}
                <nav className="flex flex-1 flex-col gap-2 p-4">

                  {links.map((link) => {
                    const Icon = link.icon;

                    return (
                      <Link
                        key={link.title}
                        href={link.href}
                        className="
                          flex
                          items-center
                          gap-3
                          rounded-xl
                          px-4
                          py-3
                          text-base
                          font-medium
                          transition-all
                          hover:bg-muted
                          hover:text-primary
                        "
                      >
                        <Icon className="h-5 w-5" />

                        <span>{link.title}</span>
                      </Link>
                    );
                  })}

                </nav>

                {/* Footer */}
                <div className="border-t p-6">
                  <p className="text-center text-sm text-muted-foreground">
                    Virtual Mall
                  </p>

                  <p className="mt-1 text-center text-xs text-muted-foreground">
                    Expo Técnico Profesional
                  </p>
                </div>

              </div>

            </SheetContent>
          </Sheet>
        </div>

      </div>
    </header>
  );
}