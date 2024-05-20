import { useState } from 'react'
import './App.css'

function App() {
  const [url, setUrl] = useState('')
  const [qrcode, setQrcode] = useState(null)
  const [isLoading, setIsLoading] = useState(false)

  const submit = async () => {
    if (url === '') {
      return
    }
    setIsLoading(true)
    try {
      const response = await fetch('http://localhost:8000/generate', {
        method: "POST",
        body: JSON.stringify({url}),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      const data = await response.json()
      console.log(data)
      setQrcode(`data:image/svg+xml;base64,${data.qrcode}`)
    } catch (error) {
      console.error(error)
    } finally {
      setIsLoading(false)
    }
  }
  return (
    <>
      <h1 className='title'>Generate QR</h1>
      <input
        className='input'
        type="text"
        value={url}
        onChange={e => setUrl(e.target.value)}
      />
      <button
        className='submit'
        onClick={submit}
      >
        Generate
      </button>
      {isLoading &&
        <span>Loading ...</span>
      }
      {qrcode !== null &&
        <img
          className='result'
          src={qrcode}
          alt="QRCode"
          width="200"
          height="200"
        />
      }

    </>
  )
}

export default App
