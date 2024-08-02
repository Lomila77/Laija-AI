import React from "react";
import  { Link } from "react-router-dom";
import Avatar from "./avatar";
import AccentButtonXL from "./button/accent-button-xl";
import LaijaAI from "../assets/Laija/logo.png";
import ThemeController from "./theme-controller";

const Header: React.FC = () => {
  return (
    <div className="navbar bg-neutral p-4">
        <Link to="/">
            <img src={LaijaAI} alt="LaijaAI" className="size-20" />
        </Link>
        <AccentButtonXL text="LaijaAI" to="/"/>
        <ThemeController />
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
                    <li><a>Logout</a></li>
                </ul>
            </div>
        </div>
    </div>
  );
};

export default Header;
