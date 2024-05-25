import { useState } from 'react'
import useFetch from './Hooks/useFetch'
import './App.css'

function App() {
  const [url, setUrl] = useState('')
  const [qrcode, setQrcode] = useState(null)
  const { fetching, isLoading } = useFetch()

  const submit = async () => {
    if (url === '') {
      return
    }
    const data = await fetching('http://localhost:8000/generate')
    setQrcode(`data:image/svg+xml;base64,${data.qrcode}`)

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
