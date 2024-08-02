import React from "react";
import { Link } from "react-router-dom";
import Props from "./props";

const NeutralButtonXL: React.FC<Props> = ({ text, to, submit, disabled }) => {
    return (
        <div className="flex-1">
        {to ? (
            <Link to={to}>
                <button disabled={disabled} className={`btn btn-neutral border-secondary hover:border-secondary rounded-xl text-xl text-accent inner-shadow-neutral shadow-xl font-sans font-bold`}>
                    {text}
                </button>
            </Link>
        ) : submit ? (
                <button disabled={disabled} className={`btn btn-neutral border-secondary hover:border-secondary rounded-xl text-xl text-accent inner-shadow-neutral shadow-xl font-sans font-bold`}>
                    {text}
                </button>
        ) : null
        }
    </div>
    )
}

export default NeutralButtonXL;
