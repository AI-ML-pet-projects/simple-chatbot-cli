import { ModeToggle } from "@/components/mode-toggle";

export default function Header() {
  return (
    <header className='bg-[#000034] text-white py-4'>
      <div className='container mx-auto px-4 flex items-center justify-between'>
        <div className='bg-[#e60028] p-2 mr-4 rounded-sm'>
          <h1 className='text-xl font-bold'>RMIT</h1>
        </div>
        <h2 className='text-xl'>RMIT Assistant</h2>
        <ModeToggle />
      </div>
    </header>
  );
}
