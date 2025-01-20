import { useState } from 'react'
import useGenerate from './Hooks/useGenerate'
import InputText from './Components/InputText'

function App() {
  const [payload, setPayload] = useState('')
  const { data, isLoading, error, generate } = useGenerate()

  const submit = () => {
    generate('http://localhost:8000/codes/generate/', payload)
  }

  const reset = () => {
    window.location = ''
  }

  const handleChange = e => setPayload(e.target.value)
  return (
    <>
      <h1 className='title'>Generate QR</h1>
      <InputText
        value={payload}
        onChange={handleChange}
        error={error?.payload}
      />
      <button
        className='button'
        onClick={reset}
      >
        Reset
      </button>
      <button
        className='button is-primary'
        onClick={submit}
      >
        Generate
      </button>
      {isLoading &&
        <span>Loading ...</span>
      }
      {data !== null &&
        <img
          src={`data:image/svg+xml;base64,${data.qrcode}`}
          alt="QRCode"
          width="200"
          height="200"
        />
      }

    </>
  )
}

export default App
