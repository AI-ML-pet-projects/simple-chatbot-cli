export default function Footer() {
  return (
    <footer className='bg-[#000034] text-white py-4 mt-auto'>
      <div className='container mx-auto px-4 text-center'>
        <p>
          Copyright © {new Date().getFullYear()} RMIT University | Developed by{" "}
          <a href='#' target='_blank' rel='noopener noreferrer'>
            🚀 FiveG 🐝
          </a>
        </p>
      </div>
    </footer>
  );
}
