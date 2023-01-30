window.addEventListener('load', () => {
  document.querySelector('input[name=password]').addEventListener('keyup', (e)=> {
    const value = e.target.value;
    window.localStorage.setItem('password', value);
  });

  const password = window.localStorage.getItem('password');
  if (password) {
    document.querySelector('input[name=password]').value = password;
  }
});
