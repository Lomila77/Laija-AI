import React from 'react';
import PlankL from '../components/plank/plank-l';
import CadreM from '../components/cadre/cadre-m';
import LaijaCoucher from '../assets/Laija/coucher.png'
import LaijaDebout from '../assets/Laija/debout.png'
import NeutralButtonXL from '../components/button/neutral-button-xl';

const Home: React.FC = () => {
  const isConnected = localStorage.getItem('token') ? true : false;
  return (
    <PlankL componentChildren={
      <div className='flex flex-col items-start justify-start'>
        <h1 className="text-4xl font-bold mb-5 text-neutral inner-text-shadow-lg font-sans">Bienvenue sur LaijaAi !</h1>
        <h2 className="text-2xl font-bold mb-4 text-neutral inner-text-shadow-lg font-sans">Créer ton inteligence artificielle personnalisée !</h2>
        <div className="flex flex-row items-center justify-between w-full">
          <p className="text-lg mb-3 font-semibold font-sans">Choisis ses traits de caractère et son histoire !</p>
          <CadreM componentChildren={
            <img src={LaijaCoucher} alt="Laija coucher" />
          } />
        </div>
        <div className="flex flex-row items-center justify-between w-full">
          <p className="text-lg mb-3 font-semibold font-sans">Joyeuse ? Excentrique ? Complètement déjantée ?</p>
          <CadreM componentChildren={
            <img src={LaijaDebout} alt="Laija debout" />
          } />
        </div>
        <div className="flex flex-row items-start justify-start">
          <NeutralButtonXL text="LogIn" to={isConnected ? '/' : '/login'} disabled={isConnected}/>
          <div className='mr-5' />
          <NeutralButtonXL text="SignUp" to={isConnected ? '/' : '/sign-up'} disabled={isConnected}/>
        </div>
      </div>
    } />
  );
};

export default Home;
