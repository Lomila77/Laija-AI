import React from "react";
import { Link } from "react-router-dom";
import Props from "./props";

const AccentButtonXL: React.FC<Props> = ({ text, to, submit, disabled }) => {
    return (
        <div className="flex-1">
            {to ? (
                <Link to={to}>
                    <button disabled={disabled} className={`btn btn-accent border-black hover:border-black rounded-xl text-xl text-white inner-shadow-accent font-sans font-extrabold`}>
                        {text}
                    </button>
                </Link>
            ) : submit ? (
                    <button disabled={disabled} className={`btn btn-accent border-black hover:border-black rounded-xl text-xl text-white inner-shadow-accent font-sans font-extrabold`}>
                        {text}
                    </button>
            ) : null
            }
        </div>
    )
}

export default AccentButtonXL;
