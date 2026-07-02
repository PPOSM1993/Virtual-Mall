import Link from "next/link";
import { Store } from "lucide-react";

export default function Logo() {
  return (
    <Link
      href="/"
      className="flex items-center gap-3 transition-opacity hover:opacity-80"
    >
      <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-primary text-primary-foreground">
        <Store className="h-5 w-5" />
      </div>

      <div className="flex flex-col leading-none">
        <span className="text-lg font-bold">Virtual Mall</span>
        <span className="text-xs text-muted-foreground">
          Expo TP 2026
        </span>
      </div>
    </Link>
  );
}