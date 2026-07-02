import Image from "next/image";



import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <>
      {/* Hero */}
      <section className="bg-gradient-to-b from-muted/40 to-background">
        <div className="mx-auto flex min-h-[80vh] max-w-7xl items-center px-6 py-24">

          <div className="max-w-3xl">


            <h1 className="mt-8 text-6xl font-bold leading-tight">
              Descubre empresas,
              productos y servicios
              en un solo lugar.
            </h1>

            <p className="mt-6 text-lg text-muted-foreground">
              Recorre nuestro mall virtual, visita stands digitales y conoce
              las empresas participantes de la Expo Técnico Profesional.
            </p>

            <div className="mt-10 flex gap-4">
              <Button size="lg">
                Explorar Empresas
              </Button>

              <Button
                variant="outline"
                size="lg"
              >
                Ver Categorías
              </Button>
            </div>

          </div>

        </div>
      </section>

    </>
  );
}