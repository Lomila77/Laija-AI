import  { Link } from "react-router-dom";
import Avatar from "./Avatar";
import Button from "./Button";
import LaijaAI from "../assets/Laija/logo.png";
import { ACCESS_TOKEN } from "../constants";
import { useState, useEffect } from "react";

const Header = () => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        setIsAuthenticated(!!token);
        const interval = setInterval(() => {
            const currentToken = localStorage.getItem(ACCESS_TOKEN);
            setIsAuthenticated(!!currentToken);
        }, 1000);
        return () => clearInterval(interval);
    }, []);
    
    return (
        <div className="navbar bg-neutral p-4">
            <Link to="/">
                <img src={LaijaAI} alt="LaijaAI" className="size-20" />
            </Link>
            <Button theme={"dark"} text="LaijaAI" to="/"/>
            { isAuthenticated ? (
                <div>
                    <div className="mr-4"/>
                    <div className="flex-none gap-2">
                        <div className="dropdown dropdown-end ">
                            <div tabIndex={0}>
                                <Avatar />
                            </div>
                            <ul tabIndex={0} className="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
                                <li>
                                    <a className="justify-between">
                                        Profile
                                        <span className="badge">New</span>
                                    </a>
                                </li>
                                <li><a>Settings</a></li>
                                <li><a href="/logout">Logout</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            ) : <div/>}
        </div>
    );
};

export default Header;
