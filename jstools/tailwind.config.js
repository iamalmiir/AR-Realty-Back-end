/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['../ar_realty/static/css/**/*.css', '../templates/**/*.{html,js}'],
  theme: {
    extend: {
      fontFamily: {
        montserrat: ['Montserrat', 'sans-serif'],
      },
      colors: {
        primaryDark: '#0077b6',
        primaryLight: '#457b9d',
        bgDark: '#1B2430',
        accentDark: '#f77f00',
        accentLight: '#0A0A0A',
      },
    },
  },
  plugins: [],
}
