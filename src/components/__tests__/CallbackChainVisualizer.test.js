import React from 'react';
import {shallow} from 'enzyme';
import CallbackChainVisualizer from '../CallbackChainVisualizer.react';

describe('CallbackChainVisualizer', () => {

    it('renders', () => {
        const component = shallow(<CallbackChainVisualizer dot="digraph G { a -> b; }"/>);
        expect(component).to.be.ok;
    });
});
