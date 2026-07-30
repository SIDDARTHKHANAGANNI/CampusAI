import { Loader2 } from "lucide-react";
import { cn } from "@/lib/utils";

interface SpinnerProps {
  className?: string;
}

export function Spinner({ className }: SpinnerProps) {
  return (
    <div className={cn("flex justify-center items-center p-4", className)}>
      <Loader2 className="w-6 h-6 animate-spin text-violet-500" />
    </div>
  );
}
