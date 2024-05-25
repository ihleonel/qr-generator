import { useState } from "react"

const useFetch = () => {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const fetching = async (url, payload) => {
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
      setError(error)
    } finally {
      setIsLoading(false)
    }
  }
  return {fetching, isLoading, error}
}

export default useFetch
