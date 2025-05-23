import React from 'react';
import Plank from '../components/plank/plank-l';
import CadreM from '../components/cadre/cadre-m';
import LaijaCoucher from '../assets/Laija/coucher.png'
import LaijaDebout from '../assets/Laija/debout.png'
import NeutralButtonXL from '../components/button/neutral-button-xl';

const Test: React.FC = () => {
  return (
    <Plank componentChildren={
      <p>Test</p>
    } />
  );
};

export default Test;
