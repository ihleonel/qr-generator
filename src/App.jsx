import { useState } from 'react'
import './App.css'

function App() {
  const [url, setUrl] = useState('')
  const [qrcode, setQrcode] = useState(null)

  const submit = async () => {
    if (url === '') {
      return
    }
    try {
      const response = await fetch('http://localhost:8000/generate', {
        method: "POST",
        body: JSON.stringify({url}),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      const data = await response.json()
      setQrcode(`data:image/svg+xml;base64,${data.qrcode}`)
    } catch (error) {
      console.error(error)
    }
  }
  return (
    <>
      <h1>Generate QR</h1>
      <input
        type="text"
        value={url}
        onChange={e => setUrl(e.target.value)}
      />
      <button
        onClick={submit}
      >
        Generate
      </button>
      {qrcode !== null &&
        <img
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
