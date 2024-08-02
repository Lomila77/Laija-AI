import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import PlankL from '../components/plank/plank-l';
import NeutralButtonXL from '../components/button/neutral-button-xl';
import UsernameInput from '../components/input/username';
import PasswordInput from '../components/input/password';

const Login: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/users/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
        //credentials: 'include',
      });

      if (!response.ok) {
        console.error('Error from server: ', response.status, response.statusText);
        alert('Error');
        return;
      }

      const data = await response.json();
      localStorage.setItem('token', data.access);
      navigate('/');
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
      alert('Error');
    }
  };
  return (
    <PlankL componentChildren={
      <div className='flex flex-col items-start justify-start'>
        <h1 className="text-4xl font-bold text-neutral inner-text-shadow-lg font-sans">Bienvenue sur LaijaAi !</h1>
        <div className='mb-5'/>
        <h2 className="text-3xl font-bold text-neutral inner-text-shadow-lg font-sans">Login :</h2>
        <div className='mb-4'/>
        <form onSubmit={handleSubmit} className='flex flex-col items-start justify-start'>
          <label className='text-xl font-bold font-sans'>Username</label>
          <div className='mb-2'/>
          <UsernameInput
            onChange={setUsername}
          />
          <div className='mb-3'/>
          <label className='text-xl font-bold font-sans'>Password</label>
          <div className='mb-2'/>
          <PasswordInput
            onChange={setPassword}
          />
          <div className='mb-4'/>
          <NeutralButtonXL text="Login" submit={(e) => handleSubmit(e)}/>
        </form>
      </div>
    } />
  );
};

export default Login;
