export default function TypingIndicator() {
  return (
    <div className='flex justify-start mb-4'>
      <div className='max-w-[80%] p-3 rounded-lg bg-[#000034] text-white'>
        <div className='flex space-x-2'>
          <div className='w-2 h-2 rounded-full bg-white animate-bounce'></div>
          <div
            className='w-2 h-2 rounded-full bg-white animate-bounce'
            style={{ animationDelay: "0.2s" }}
          ></div>
          <div
            className='w-2 h-2 rounded-full bg-white animate-bounce'
            style={{ animationDelay: "0.4s" }}
          ></div>
        </div>
      </div>
    </div>
  );
}
