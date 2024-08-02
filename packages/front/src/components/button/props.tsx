import React, { FormEvent } from "react";

interface Props {
    text: string;
    to?: string;
    submit?: (event: FormEvent<HTMLFormElement>) => Promise<void>;
    disabled?: boolean;
}

export default Props;
