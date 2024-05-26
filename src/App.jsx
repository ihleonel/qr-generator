import { useState } from 'react'
import useGenerate from './Hooks/useGenerate'
import './App.css'

function App() {
  const [payload, setPayload] = useState('')
  const [qrcode, setQrcode] = useState(null)
  const { generate, isLoading } = useGenerate()

  const submit = async () => {
    if (payload === '') {
      return
    }
    const data = await generate('http://localhost:8000/generate', payload)
    setQrcode(`data:image/svg+xml;base64,${data.qrcode}`)

  }
  return (
    <>
      <h1 className='title'>Generate QR</h1>
      <input
        className='input'
        type="text"
        value={payload}
        onChange={e => setPayload(e.target.value)}
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
