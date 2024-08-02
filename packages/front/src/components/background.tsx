import React from "react";

interface BackgroundProps {
    componentChildren: React.ReactNode;
}

const Background = ({ componentChildren }: BackgroundProps) => {
    return (
        <div className="flex flex-col items-center justify-center p-8 bg-neutral shadow-lg w-full">
            {componentChildren}
        </div>
    )
}

export default Background;
