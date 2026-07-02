import {
  Mail,
  Phone,
  MapPin,

  Globe,
} from "lucide-react";

import {
  FaInstagram,
  FaFacebook,
  FaYoutube,
  FaLinkedin,
} from "react-icons/fa";

import { FaXTwitter } from "react-icons/fa6";

import { Button } from "@/components/ui/button";

export default function Footer() {
  return (
    <footer className="border-t bg-background">
      <div className="mx-auto max-w-7xl px-6 py-12">

        <div className="grid gap-10 md:grid-cols-4 sm:grid-cols-2">

          {/* Branding */}
          <div>
            <h2 className="text-lg font-semibold">Virtual Mall</h2>
            <p className="mt-3 text-sm text-muted-foreground">
              Plataforma interactiva del centro comercial digital para Expo TP.
            </p>

            <Button className="mt-5 w-full">
              Asistente Virtual 💬
            </Button>
          </div>

          {/* Contacto */}
          <div>
            <h3 className="mb-3 text-sm font-semibold">Contacto</h3>

            <ul className="space-y-3 text-sm text-muted-foreground">
              <li className="flex items-center gap-2">
                <Phone className="w-4 h-4" />
                +56 4 5229 7900
              </li>

              <li className="flex items-center gap-2">
                <MapPin className="w-4 h-4" />
                Av. Alemania 0671, Temuco
              </li>

              <li className="flex items-center gap-2">
                <Mail className="w-4 h-4" />
                contacto@virtualmall.cl
              </li>
            </ul>
          </div>

          {/* Enlaces */}
          <div>
            <h3 className="mb-3 text-sm font-semibold">Enlaces</h3>

            <ul className="space-y-2 text-sm text-muted-foreground">
              <li className="hover:text-foreground cursor-pointer">Tiendas</li>
              <li className="hover:text-foreground cursor-pointer">Eventos</li>
              <li className="hover:text-foreground cursor-pointer">Promociones</li>
              <li className="hover:text-foreground cursor-pointer">Mapa del mall</li>
            </ul>
          </div>

          {/* RRSS con ICONOS */}
          <div>
            <h3 className="mb-3 text-sm font-semibold">Síguenos</h3>

            <div className="flex gap-3 mt-2">

              <a
                href="#"
                className="p-2 rounded-full bg-muted hover:bg-primary hover:text-white transition"
              >
                <FaInstagram className="w-8 h-8" />
              </a>

              <a
                href="#"
                className="p-2 rounded-full bg-muted hover:bg-primary hover:text-white transition"
              >
                <FaFacebook className="w-8 h-8" />
              </a>

              <a
                href="#"
                className="p-2 rounded-full bg-muted hover:bg-primary hover:text-white transition"
              >
                <FaXTwitter className="w-8 h-8" />
              </a>

              <a
                href="#"
                className="p-2 rounded-full bg-muted hover:bg-primary hover:text-white transition"
              >
                <FaYoutube className="w-8 h-8" />
              </a>

              <a
                href="#"
                className="p-2 rounded-full bg-muted hover:bg-primary hover:text-white transition"
              >
                <FaLinkedin className="w-8 h-8" />
              </a>

            </div>
          </div>
        </div>

        {/* Bottom bar */}
        <div className="mt-10 border-t pt-6 flex flex-col gap-3 md:flex-row md:justify-between text-xs text-muted-foreground">
          <p>© 2026 Virtual Mall. Todos los derechos reservados.</p>
          <p>Proyecto Expo Técnico Profesional</p>
        </div>

      </div>
    </footer>
  );
}