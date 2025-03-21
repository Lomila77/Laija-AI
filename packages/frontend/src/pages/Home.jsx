import Plank from '../components/Plank';
import Cadre from '../components/Cadre';
import LaijaCoucher from '../assets/Laija/coucher.png'
import LaijaDebout from '../assets/Laija/debout.png'
import Button from '../components/Button';
import { ACCESS_TOKEN } from "../constants"
import Title from "../components/Title"
import Text from "../components/Text"


function Home() {
    const isAuthenticate = localStorage.getItem(ACCESS_TOKEN) ? true : false;

    return <Plank componentChildren={
        <div className='flex flex-col items-start justify-start'>
            <Title size={"large"} content={"Bienvenue sur LaijaAi !"} />
            <Title size={"medium"} content={"Créer ton inteligence artificielle personnalisée !"} />
            <div className="flex flex-row items-center justify-between w-full">
                <Text theme={"dark"} content={"Choisis ses traits de caractère et son histoire !"} />
                <Cadre size={"large"} componentChildren={
                    <img src={LaijaCoucher} alt="Laija coucher" />
                } />
            </div>
            <div className="flex flex-row items-center justify-between w-full">
                <Text theme={"dark"} content={"Joyeuse ? Excentrique ? Complètement déjantée ?"} />
                <Cadre size={"large"} componentChildren={
                    <img src={LaijaDebout} alt="Laija debout" />
                } />
            </div>
            <div className="flex flex-row items-start justify-start">
                <Button theme={"light"} text="LogIn" to={isAuthenticate ? '/' : '/login'} disabled={isAuthenticate}/>
                <div className='mr-5' />
                <Button theme={"light"} text="Register" to={isAuthenticate ? '/' : '/sign-up'} disabled={isAuthenticate}/>
            </div>
        </div>
    } />
}

export default Home;