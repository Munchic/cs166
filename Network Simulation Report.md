## Network Simulation Report

### Part 1: Model modifications

#### Introduced modifications and assumptions

##### Normal distributions (individuality)

In a real world scenario, we can have a community (club) that on average has some open-mindedness ($\alpha$), easy goingness ($\beta$) and stubbornness ($\gamma$) but in reality each individual carries a slightly different set of these traits. We introduce sampling from normal distribution for all parameters to introduce some noise that more closely resembles a real world heterogenous community.

We will sample ($\alpha_i, \beta_i, \gamma_i$) with constant variance $\sigma^2$:

- $\alpha_i\  ͠\ N(\alpha, \sigma^2)$
- $\beta_i\  ͠\ N(\beta, \sigma^2)$
- $\gamma_i\  ͠\ N(\gamma, \sigma^2)$
- $\sigma = 0.05 \text{ (heterogeneity)}$

One small tweak is that the samples ($\alpha_i, \beta_i, \gamma_i$) have to come from truncated normal distributions that preserve the original range of these parameters.

Constraints to these variables remain the same as in the original model:

- $\alpha_i \in (0, 0.5]$
- $\beta_i \in (0, 1)$
- $\gamma_i \in [0, 1+\beta_i^{-1})$

##### Persuasiveness

Apart from open-mindedness, as conversationalists, we pay attention to how persuasive is the person we’re speaking to (neighbor). In this addition, we will assume the neighbor’s persuasiveness is weighted with $1-\alpha_i$; this will mean that when a listener is open-minded, it does not matter much how good or bad the neighbor is at persuading. Reversedly, if a listener is very close-minded, a non-persuasive speaker will further decrease opinion change, and a very persuasive speaker can increase opinion change. We will call this variable $\nu_j$ defined per neighbor, also sampled from $\nu_j  ͠\ N(\eta, \sigma^2)$.

The constraints and properties of $\nu_ j$ is the following:

- $\nu_j \in [0, 1]$
- $\text{if (}\nu_j = 0.5 \text{) ⇒ average persuasiveness, does not facilitate opinion change}$

##### Self-research

Internet and physical libraries are widely available to most people in the world; thus, after a good conversation, we are likely to do more research on our own. We will assume that the opinion change due to self-research occurs “by chance” — only if a person does research (let’s say $c=10\%$ of the time). Usually, self-research is more likely after a good interaction so we can further weight the research chance by the weight of the relationship, $w_{ij}$. The main coefficient here would be $\eta_ i$ which is the normalized learning coefficient along with $r=0.1$ which is an adjustment to keep $\eta_i$ within a pretty numeric range.

Of course, self-research cannot happen without confirmation bias, so $b_i$ would indicate the direction of bias ($-1$ or $+1$), and the chance of direction is directly proportional to how biased the existing opinion is. Mathematically speaking, we can represent this bias as $\begin{cases} p(b_i=+1) = o_i \\  p(b_i=-1) = 1-o_i \end{cases}$ which leads to $E[b_i] = +1(o_i) - 1(1-o_i)$. The total contribution of self-research to opinion change would be $cw_{ij}(r\eta_ib_i)$. 

The constaints and values for the parameters in this terms are the following:

- $\eta_i \in [0, 1]$
- $b_i \in \{-1, 1\}$ 
- $c=0.1$
- $r = 0.1$

#### Update rules

The original update equations for the social network model are:
$$
\begin{cases}	\Delta o_i=\alpha w_{ij}(o_j - o_i) \\	\Delta w_{ij} = \beta w_{ij}(1 - w_{ij})*(1 - \gamma |o_i-o_j|)\end{cases}
$$
With the first modification, we add **individuality** to each node’s parameters, therefore, now $\alpha, \beta, \gamma$ would be indexed per node and are sampled from truncated normal distributions $\alpha_i \in (0, 0.5], \beta_i \in [0, 1]$, and $\gamma_i \in [0, 1+\beta_i^{-1})$:
$$
\begin{cases}	\Delta o_i=\alpha_i w_{ij}(o_j - o_i) \\	\Delta w_{ij} = \beta_i w_{ij}(1 - w_{ij})*(1 - \gamma_i |o_i-o_j|) \\	\alpha_i\   ͠ \ N(\alpha, \sigma),\  \beta_u\   ͠ \ N(\beta, \sigma),\ \gamma_i\   ͠ \ N(\gamma, \sigma) \\	\sigma = 0.05 \text{ (standard deviation of the sampling)}\end{cases}
$$
When we introduce **persuasiveness** ($\nu$) of the neighbor, we change the coefficient for opinion update:
$$
\begin{cases}	\Delta o_i=[\alpha_i + (1-\alpha_i)(\nu_j - 0.5)] w_{ij}(o_j - o_i) \\	\Delta w_{ij} = \beta_i w_{ij}(1 - w_{ij})*(1 - \gamma_i |o_i-o_j|)\end{cases} \\ ~ \\\begin{cases}	\Delta o_i=[1.5\alpha_i+\nu_j(1-\alpha_i)-0.5] w_{ij}(o_j - o_i) \\	\Delta w_{ij} = \beta_i w_{ij}(1 - w_{ij})*(1 - \gamma_i |o_i-o_j|)\end{cases}
$$
When we introduce how much **self-research** can convince oneself ($\eta$), we add an additional term to opinion change based on self-research (let’s examine the expected average case):
$$
\begin{cases}	\Delta o_i=[1.5\alpha_i+\nu_j(1-\alpha_i)-0.5] w_{ij}(o_j - o_i)+ cw_{ij}(r\eta_i E[b_{i}]) \\	E[b_{i}] =  +1(o_{i}) -1(1-o_{i}) \text{ (bias direction)} \\	\Delta w_{ij} = \beta_i w_{ij}(1 - w_{ij})*(1 - \gamma_i |o_i-o_j|) \\	c = 0.1 \text{ (chance that one will research)} \\ 	r = 0.1 \text{ (coefficient of opinion change due to research)}\end{cases} \\ ~ \\\begin{cases}	\Delta o_i=w_{ij}[(1.5\alpha_i+\nu_j(1-\alpha_i)-0.5) (o_j - o_i)+ k\eta_i (2o_i - 1)] \\	\Delta w_{ij} = \beta_i w_{ij}(1 - w_{ij})*(1 - \gamma_i |o_i-o_j|) \\	k = rc = 10^{-2} \text{ (cumulative coefficient)}\end{cases}
$$
Finally, the aggregated update equations look as such:
$$
\\\begin{cases}	\Delta o_i=w_{ij}[(1.5\alpha_i+\nu_j(1-\alpha_i)-0.5) (o_j - o_i)+ 0.01\eta_i (2o_i - 1)] \\	\Delta w_{ij} = \beta_i w_{ij}(1 - w_{ij})*(1 - \gamma_i |o_i-o_j|)
\end{cases}
$$

### Part 2: Local analysis

#### Relationship between two nodes

##### Individual model parameters

This setting will not change the average behavior of the network for the majority of parameter settings because all variables are distributed normally (except for edge cases near 0 or maximum). For edge cases, the relationship will be more “smoothed out” and more similar to a less extreme case.

##### Persuasiveness

Speaker’s persuasiveness’ importance is inversely proportional to the open-mindedness of the listener. If the listener is open-minded, the speakers' varying level persuasiveness should not affect much how opinion is changed (an open-minded person will likely listen to a bad explainer). If the listener is closer-minded, the speaker’s level of persuasion will matter much, and bad persuasion in this case would reduce opinion change drastically.

##### Self-research

Convincement based on self-research would reinforce the opinion change with higher chance in case of a good interaction (high edge weight). Therefore, opinion change (and biasedness) will happen even more strongly when the relationship is strong. Self-research, on average, will only make opinion formation between two nodes faster.

#### Parameter settings for converging and diverging opinion

##### Persuasiveness

As we observe in the formula for opinion update, $a_i$ shares weight with $v_j$ meaning in an average sum. This means that even a rather close-minded person can be persuaded by a very persuasive conversationalist, and an open-minded person might be turned off by a very unpersuasive person. Let us analyze the average case for this trait.

There are three cases to observe if we keep all other parameters constant:

1. $\nu_j = 0.5$:
   This is a simple case because here, the coefficient turns into $1.5\alpha_i+\nu_i(1-\alpha_i)-0.5= \alpha_i$, meaning that the system will behave exactly like without the persuasiveness parameter. This makes sense because when everyone is average convincingness, open-mindedness dictates what opinion gets written into people’s minds. An average in terms of convincingness conversator does not help persuade one, nor does it throw them off.

2. $\nu_j < 0.5$:
   We will analyze two cases w.r.t. $\alpha$ because these two coefficients compose into the opinion change coefficient. Since thresholds for $\alpha$ is dependent on choice of $\beta, \gamma$, we will figuritavely divide cases into small $\alpha$ (diverging opinion network) and large $\alpha$ (converging opinion network).

   1. Small $\alpha_ i$:
      In this situation, because an average listener is rather close-minded, it takes persuasiveness to convince, and low persuasiveness will distract much. This means that the nodes' opinions will likely diverge because both open-mindedness and persuasiveness are low, further slowing down the convergence (compared to just low open-mindedness). Slow opinion convergence leads to faster relationship degradation.
   2. Large $\alpha _i$:
      In this situation, because an average listener is already quite open-minded, it does not take too much persuasiveness to convince, and low persuasiveness does not distract. This is reflected in the coefficient $1-\alpha_i$ for $\nu_i$.  The larger $\alpha_i$, the less prone is opinion change due to unpersuasiveness. Therefore, nodes’ opinions will more likely diverge than when $\nu_i \geq 0.5$ but if $\alpha_i$ is sufficiently large, the convergence will likely remain. An example of this situation is when very shy open-minded people talk to each other, and because they are open-minded, they are less likely to be picky about how the other person is expressing their thoughts.

3. $\nu_j > 0.5$:

   1. Small $\alpha _i$:

      Network by default diverges in opinion, but because $\nu_i > 0.5$, neighbor nodes are more persuasive, so the divergence will be slowed down and relationships stregths will remain for longer. Because the open-mindedness is low, a large weight is put on persuasiveness so for large enough $\nu_i$, the network can converge in opinion and have strong relationships.

   2. Large $\alpha_ i$:

      The network will more likely converge and have stronger relationships because by default it already converges, and the persuasiveness is high. This is similar to low-information voters who have good persuasion skills, and in the end convert to a homogenous in terms of opinion voters.

##### Self-research

Self-research happens after a conversation. If it was a good interaction (high relationship strength), both parties will likely learn more about the topic at home. The bias for learning is based on existing opinion (mroe biased towards existing opinion), so self-research will **only** foster faster opinion change.

We can analyze cases when the network diverges and converges in terms of opinion and see how self-research comes in. Let’s assume there is a small value $\epsilon$ below which the self-research would not noticeably change the average network properties of a configured network:

1. $\eta_i < \epsilon$:
   For very small self-convincing research coefficient, the update equation $\Delta o_i$ does not change. Therefore, no matter what $\alpha_i$ is, the convergence/divergence behavior of the network will stay pretty much untouched.

2. $\eta _i \geq \epsilon$:
   When self-research exists, we should consider two situations where $\alpha$ is above or below the convergence threshold for a given parametrized network (similar to how we analyzer persuasiveness).

   1. Small $\alpha_ i$:

      By default, network will diverge because learning rate is too slow to keep relationships strong (which depend on similarity of opinions). If convincement from self-research is high enough, it will boost the opinion change as $k\eta_i (2o_i - 1)$ will increase. This means that if the opinion skewing towards $0 \ (o_i < 0.5)$, then it the research on average will move the opinion futher that way; the reverse applies.
      This boost in opinion change will increase the chance of divergence. If $\alpha_ i$ is right at the threshold value, adding a high $\eta_i \to 1$ will change the network to diverging very rapidly. When difference in opinions are large (due to faster divergence of opinions), relationship strengths will decrease.

   2. Large $\alpha_ i$:
      By default, network will converge because opinion update rate is large enough to keep relationships strong (which depend on similarity of opinions). When we add in prominent self-research here, the opinions divert (polarize) faster, again, independent of other factors as stated in the first paragraph. This means that at high enough $\eta_i$, we can make a converging network diverge and weaken its relationships.

We can observe that in all prominent values of $\eta_i$, the network will more likely diverge in terms of opinion, and the relationship strength will weaken on average. Probably this can explain why in the modern day, running a single ideology is very hard (e.g., pro-life or pro-choice) because each node has high capacity to self-research creating a faster polarization in opinions and weaker intergroup relationships. 

#### Vector fields analysis

##### Experiment 1: standard model with individuality

Let us plot the vector field of the network with parameters sampled from truncated normal distribution and compare it to the vector field of the original model, with deterministic parameters. We will stick to the default parameters $\alpha = 0.03, \ \beta = 0.3, \gamma = 4$.

<img src="/Users/Munchic/Desktop/CS166/2.1a.png" alt="Screen Shot 2020-03-23 at 21.18.21" style="zoom:50%;" />

As we can see in the comparison above, the general behavior remains similar in the average case where the left part of the graph (opinion difference $< 0.4$) converges to strong relationships and zero opinion difference. This shows that the general behavior of a network model with individuality incorporated is similar to that of the deterministic one, given a small enough standard deviation. To make this analysis more strict, we can consider various combination of parameters (that lead to always convergence or always divergence).

##### Experiment 2: varying persuasiveness

Using the default parameters $\alpha = 0.03, \ \beta = 0.3, \gamma = 4$ (small alpha, divergence), let’s plot the graph for various values of persuasiveness, $\nu$.

![Screen Shot 2020-03-23 at 21.30.22](/Users/Munchic/Desktop/CS166/As3 2.2a.png)

As we predicted previously, at $\nu=0.5$, the behavior should be identical to the original model like in the original model. We also discussed that for small $\alpha$, if $\nu$ is large enough like in the rightmost panel, the convergence will happen. This is similar to the case when people are generally close-minded but are really good at persuading leading to a faster opinion convergence. At this rightmost panel, the setting leads to convergence because the majority of the graph area is green (converging).

Now, let’s try to vary persuasiveness for a larger $\alpha=0.45$. We will still hold $\beta = 0.3, \gamma = 4$.

![Screen Shot 2020-03-23 at 21.41.42](/Users/Munchic/Desktop/CS166/As3 2.2b.png)

As we can see, even when the persuation is pretty bad, because the people are so open-minded, it does not matter to them, so convergence still happens in every case. In the rightmost panel, we can see that convergence of opinion happens very rapidly. This is because the influence coefficient is dominated both by $\alpha$ and $\nu$ making the $\Delta o_i$ very large and converging fast. In the rightmost case, because the convergence is so fast, the weights “do not have time” to degrade of opinion difference. This is in line with what we predicted in the parameter setting section.

##### Experiment 3: varying convincement from self-research

This aspect cannot be visualized with the same vector field because opinion update due to self-research is dependent on the opinion value itself ($o_i$) and not the difference in opinions $(o_j - o_i)$. Therefore, we cannot use the same 2D vector field to represent how an opinion would converge because including self-research means that the update depends both on opinion difference and value of opinion itself. A 3D vector field would be required for this situation but it’s time-consuming to generate such a plot and it is hard to analyze, so we will analyze empirically in Part 4.

### Part 3: Implementation

[[Source code](https://github.com/Munchic/cs166/blob/master/As3. Opinion Network Simulation.ipynb)]

### Part 4: Simulation analysis

#### Network simulations

To run the simulation experiments on the real network, we create a Watts-Strogatz small-world random network graph with $30$ nodes, average neighbor connectivity of $5$, and randomness (probability of rewiring each edge) at $0.5$. Watts-Strogatz is a suitable graph type to model opinion exchange in humans because we tend to have small groups of friends and a few intergroup connections (friend of a friend from another close group of friends). This would allow a rather realistic simulation of how opinion formation happens within a group of people given certain characteristics (parameters of the model).

##### Experiment 1: standard model with individuality

Similarly to the experimentation with vector field, we can confirm with the plot below that switching on sampling of parameters with a small standard deviation does not change the overall behavior much. In the diverging parameters of  $\alpha = 0.03, \ \beta = 0.3, \gamma = 4$, we get divergence of groups where the opinions are about $0.25$ and $0.75$. Analogously, we can verify for convergent networks that they behave similarly in `original` and `individuality` models.

![Screen Shot 2020-03-23 at 22.02.19](/Users/Munchic/Desktop/CS166/As3 4.1a.png)



##### Experiment 2: varying persuasiveness

Per parameter values analysis, we will divide into cases of small $\alpha$ (divergence) and large $\alpha$ (convergence). In the case of divergence, we can observe in the graph below that it exhibits similar behavior to the vector field analysis — that is, when persuasiveness is low, it “turns off” opinion update, and thus, we have divergence. When persuasiveness $\nu=0.5$, the graph is quite similar to the first case: slower divergence with a less extreme cluster opinion (about $0.35$ and $0.65$). In case when persuasiveness is high (last row), everyone convinces each other to believe in the middle opinion.

![Screen Shot 2020-03-23 at 22.12.49](/Users/Munchic/Desktop/CS166/As3 4.2a.png)

Let us try the same experiment on large $\alpha=0.45$, with the same $\beta = 0.3, \gamma = 4$:

![Screen Shot 2020-03-23 at 22.19.59](/Users/Munchic/Desktop/CS166/As3 4.2b.png)

Confirming the prediction with vector fields, when open-mindedness is high, persuasiveness plays less of a role. Even when persuasiveness is very low ($\nu = 0.1$), we still have convergence due to high $\alpha$ although the convergence is slightly slower. With high $\nu = 0.9$, we get very fast convergence (not observable in this graph, but if we reduce number of steps between frames, we will see).

##### Experiment 3: varying convincement from self-research

Let’s now vary the parameter for ability to convince oneself during self-research. We will try the case with small $\alpha = 0.03$ first.

![Screen Shot 2020-03-23 at 22.33.15](/Users/Munchic/Desktop/CS166/As3 4.3a1.png)

As we can see, the behavior is very interesting. For small enough self-convincement, the graphs do not change much, there is still a divergence even though it has a smaller difference in group opinions. In cases of larger $\eta$  (when $\alpha$ is small), we do indeed see the weakening of relationships. What is interesting to note is that in 3rd and 4th rows of the figure above, there are clusters with similar opinions yet they do not have a relationship. This could be due to the fact that self-researching nodes can “research themselves out of the group” — meaning that the change in opinion could be so large that iterative separation from groups can occur. In 4rd row, it seems like the discrete purple nodes self-researched themselves independently out of the main group. This can happen because the main cluster has neutral or closer to $0$ opinion, meaning that bias can go either way, and once the direction is chosen, a positive reinforcement will likely occur. 

Let’s apply the same analysis to the case of large $\alpha$. The simulation was cut shorter to $10,000$ steps per frame because there were computational constraints:

![Screen Shot 2020-03-23 at 22.58.47](/Users/Munchic/Desktop/CS166/As3 4.3b.png)

Here we can see that network behaves similarly for all $\eta$ unlike how we predicted in Part 2. This might be because they are so open-minded that they have an fast opinion convergence together and strengthen connectivity (relationships).

#### Comparison to real-life patterns

##### Persuasiveness

The simulations show that persuasiveness matters when a group is close-minded and does not matter too much when a group is open-minded. This is similar to a real-life situation when we try to convince a group of children (high $\alpha$) to believe in something (e.g., Santa Claus exists), and their opinion easily sway even if the way to persuade is not fluent. In contrast, among reasoning adults (low $\alpha$), it would be hard to convince them to believe in something without good persuation tactics.

##### Self-research

We saw that self-research can create really unpredictable dynamics in the groups. The scenario of small $\alpha$ and large $\eta$ resembles a case where high-class scientists (generally, close-minded or picky) research a topic together and unknowingly independently discover a new vision (e.g., calculus) without being in a group together. This then creates like-minded small clusters/individual nodes that do not have strong relationship because they independently came out of a group of a more neutral opinion. 

