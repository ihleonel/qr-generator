// eslint-disable-next-line react/prop-types
function InputText({value, onChange, placeholder, error}) {
  const inputClass = () => {
    let cls = 'input'
    if (error) {
      cls = `${cls} is-danger`
    }
    return cls
  }
  return (
    <>
      <input
        type="text"
        value={value}
        placeholder={placeholder}
        onChange={onChange}
        className={inputClass()}
      />
      <p className="help is-danger">
        {error}
      </p>
    </>
  )
}

export default InputText
