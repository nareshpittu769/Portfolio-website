

  const scriptURL = 'https://script.google.com/macros/s/AKfycbzSQUPFARujVevKWGFRU2TToO3NVkDZ9_RxF-diik_Ps7-n_WH52JHdTZqv_RheOKjoYw/exec'
  const form = document.forms['submit-to-google-sheet']
  const msg = document.getElementById('msg')
  form.addEventListener('submit', e => {
    e.preventDefault()
    fetch(scriptURL, { method: 'POST', body: new FormData(form)})
      .then(response => {
        msg.innerHTML = 'Message sent successfully'
        setTimeout(()=>{
            msg.innerHTML = ''
        }, 5000)
        form.reset()
      })
      .catch(error => console.error('Error!', error.message))
  })

