import { useState } from "react"

const useGenerate = () => {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const generate = async (url, payload) => {
    setIsLoading(true)
    try {
      const response = await fetch(url, {
        method: "POST",
        body: JSON.stringify({payload}),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      const data = await response.json()
      return data
    } catch (error) {
      console.error(error)
    } finally {
      setIsLoading(false)
    }
  }
  return {generate, isLoading, error}
}

export default useGenerate
