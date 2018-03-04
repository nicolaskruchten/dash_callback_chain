import React, {Component} from 'react';
import {CallbackChainVisualizer} from '../src';

class Demo extends Component {
    constructor() {
        super();
        this.state = {
            value: ''
        }
    }

    render() {
        return (
            <div>
                <h1>dash-callback-chain Demo</h1>

                <hr/>
                <h2>CallbackChainVisualizer</h2>
                <CallbackChainVisualizer
                    dot="digraph G { a -> b; }"
                    setProps={newProps => this.setState({value: newProps.value})}
                />
                <hr/>
            </div>
        );
    }
}

export default Demo;
