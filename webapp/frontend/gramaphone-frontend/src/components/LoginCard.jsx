import React from 'react'
const LoginCard = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const HandleSubmit = () => {
        
    }

  return (
    <>
      <div className="flex items-center justify-center min-h-screen bg-gray-900">
      <div className="w-full max-w-md">
        <form className="bg-gray-800 shadow-md rounded-lg px-12 pt-8 pb-8 mb-4" onSubmit={HandleSubmit}>
          <h2 className="text-3xl font-bold text-center text-white mb-6">Login</h2>
          <div className="mb-6">
            <input
              className="shadow appearance-none border rounded w-full py-3 px-4 text-gray-200 leading-tight focus:outline-none focus:shadow-outline bg-gray-700"
              id="email"
              type="email"
              placeholder="Email"
            />
          </div>
          <div className="mb-6">
            <input
              className="shadow appearance-none border rounded w-full py-3 px-4 text-gray-200 mb-3 leading-tight focus:outline-none focus:shadow-outline bg-gray-700"
              id="password"
              type="password"
              placeholder="Password"
            />
          </div>
          <div className="flex items-center justify-between mb-6">
            <button
              className="bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-4 rounded focus:outline-none focus:shadow-outline w-full transition duration-300 ease-in-out transform hover:scale-105"
              type="button"
            >
              Sign In
            </button>
          </div>
          <div className="text-center">
          </div>
        </form>
        
      </div>
    </div>
    </>
  )
}

export default LoginCard
