import { type ComponentType } from "react";
import { ReactNode } from "react";

interface EmptyStateProps {
  icon: ComponentType<{ className?: string; size?: number }>;
  title: string;
  description: string;
  action?: ReactNode;
}

export function EmptyState({ icon: Icon, title, description, action }: EmptyStateProps) {
  return (
    <div className="flex flex-col items-center justify-center p-12 text-center">
      <div className="bg-stone-50 p-4 rounded-full mb-4">
        <Icon className="w-8 h-8 text-stone-300" />
      </div>
      <h3 className="text-lg font-semibold text-stone-800 mb-1">{title}</h3>
      <p className="text-stone-400 mb-6 max-w-sm">{description}</p>
      {action && <div>{action}</div>}
    </div>
  );
}
