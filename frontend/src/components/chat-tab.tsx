import { cn } from "@/lib/utils";
import { MessageSquare, X } from "lucide-react";
import { ChatSession } from "@/types/chat";

interface ChatTabProps {
  session: ChatSession;
  isActive: boolean;
  onSelect: (sessionId: string) => void;
  onClose: (sessionId: string) => void;
}

export default function ChatTab({
  session,
  isActive,
  onSelect,
  onClose,
}: ChatTabProps) {
  const handleClose = (e: React.MouseEvent) => {
    e.stopPropagation();
    onClose(session.id);
  };

  const getTitle = () => {
    if (session.messages.length === 0) return "New Chat";
    const firstMessage = session.messages[0];
    return firstMessage.content.length > 20
      ? `${firstMessage.content.substring(0, 20)}...`
      : firstMessage.content;
  };

  return (
    <div
      className={cn(
        "flex items-center px-4 py-2 border-r border-gray-200 cursor-pointer group transition-colors",
        isActive
          ? "bg-white text-[#000034] font-medium"
          : "bg-gray-100 text-gray-600 hover:bg-gray-200"
      )}
      onClick={() => onSelect(session.id)}
      role='button'
      tabIndex={0}
      aria-selected={isActive}
    >
      <MessageSquare className='h-4 w-4 mr-2 flex-shrink-0' />
      <span className='truncate max-w-[150px]' title={getTitle()}>
        {getTitle()}
      </span>
      <button
        className='ml-2 opacity-0 group-hover:opacity-100 transition-opacity'
        onClick={handleClose}
        aria-label='Close chat'
      >
        <X className='h-4 w-4 text-gray-500 hover:text-gray-700' />
      </button>
    </div>
  );
}
