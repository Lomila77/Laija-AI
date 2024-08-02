import React from "react";
import Props from "./props";

const PlankL = ({ componentChildren }: Props) => {
    return (
        <div className="flex flex-col items-center justify-center bg-primary p-16 rounded-3xl shadow-lg box-border border-2 border-secondary inner-shadow-accent">
            {componentChildren}
        </div>
    )
}

export default PlankL;
