import { useState } from "react"

const useGenerate = () => {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const [data, setData] = useState(null)
  const generate = async (url, payload) => {
    if (isLoading === true) {
      return;
    }
    setError(null)
    setData(null)
    setIsLoading(true)
    try {
      const response = await fetch(url, {
        method: "POST",
        body: JSON.stringify({payload}),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      const json = await response.json()
      if (response.status === 400) {
        setError(json.errors)
      }
      if (response.status === 201) {
        setData(json)
      }
    } catch (err) {
      console.error(err)
    } finally {
      setIsLoading(false)
    }
  }

  return {data, isLoading, error, generate}
}

export default useGenerate
