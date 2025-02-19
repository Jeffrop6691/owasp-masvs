# 移动应用安全验证标准

MASVS 可以被用于确立移动应用程序的安全程度。此标准(MASVS)的建立遵循了下面三个主要目标：

- 可用于业界应用的安全度量标准 - 提供一个安全标准，让开发者和使用者们可以比较现有的移动应用程序；
- 可用于指导纲领 - 为移动应用程序整个开发阶段和测试提供安全指引；
- 可用于采购检验的验证参考 - 提供一个移动应用程序安全的验证标准。

## 移动应用安全模型 (Mobile AppSec Model)

MASVS定义了两个安全验证级别（MASVS-L1 和 MASVS-L2），以及一系列的抵抗逆向工程防御韧性准则（MASVS-R）。 MASVS-L1是建议所有的移动应用程序都应该遵守的要求，MASVS-L2则针对的是处理高度敏感数据的移动应用程序。MASVS-R提供了需要防范客户端威胁时可以使用的额外防护管控方法。

满足MASVS-L1中所提到的要求，可以确保移动应用程序的安全，使开发流程符合信息安全的最佳实践方法，并且确保移动应用程序可以防御常见的安全问题。 MASVS-L2添加了额外的纵深防御（defense-in-depth），例如证书绑定（SSL pinning）。因此，MASVS-L2可以使移动应用程序能够更好的防范复杂的攻击行为 - 假设移动操作系统的安全控件完好无损，并且最终用户不被视为潜在的恶意用户。满足全部或者部分的MASVS-R软件保护要求，可以帮助阻止特定的客户端威胁，包括最终用户是恶意用户或者手机操作系统遭到破坏的情况。

**I: 虽然我们建议应该在每一个移动应用程序中实施MASVS-L1准则，但是否实施最终应是基于风险的决策，该决策应与软件所有者沟通。**

**II: 请注意，MASVS-R和<OWASP移动安全性测试指南>中所提到的软件保护准则无法确保不被绕过，绝对不能用作安全管控的替代品。相反的，这些软件保护准则旨在增加已落实MASVS-L1或MASVS- L2的移动应用程序，针对特定的威胁提供额外的防御。**

![Verification Levels](images/masvs-levels-new.jpg)

### 文档结构

MASVS的第一部分阐述了移动应用的安全模型和可用的安全验证级别，接着是有关如何使用本标准的建议。第二部分则是阐述了安全准则的细节和和对应的安全验证级别。基于技术的的目的或范畴，此准则被分成8个类别（从V1到V8）。准则类别与条目的命名方法如下（MASVS和MASTG使用相同的方法命名）：

- *准则类别：* MASVS-Vx，例如：MASVS-V2: 数据存储和隐私
- *准则条目：* MASVS-Vx.y，例如： MASVS-V2.2: "敏感数据不应被写入应用程序日志"

### 安全验证等级细节

#### MASVS-L1: 标准安全等级

实现MASVS-L1的移动应用程序需要遵循移动应用程序安全的最佳实践方法。它包含了代码的质量，敏感数据的处理以及与移动环境交互的基本安全准则。此外，MASVS-L1必须有一个测试流程来验证安全管控。MASVS-L1适用于所有的移动应用程序。

#### MASVS-L2: 纵深防御（Defense-in-Depth）

MASVS-L2引入了高于标准要求的高级安全管控方法。为了实现MASVS-L2，首先需要有一个威胁模型，并且把安全视为应用程序的一部分，加入到应用程序的架构和设计之中。MASVS-L2适用于处理高度敏感数据的应用程序，例如手机银行应用程序。

#### MASVS-R: 抵抗逆向工程和篡改的能力

符合MASVS-R的应用程序需具有最先进的安全性，并且可以抵抗有明确定义的特定客户端攻击，例如：篡改，程序修改或者逆向工程提取敏感代码或数据。这样的应用程序需要使用硬件安全模块或者是使用足够强大且经过验证的软件保护技术。MASVS-R适用于处理高度敏感数据的应用程序，并且可以用作保护知识产权或防篡改应用程序的一种方式。

### 使用建议

基于风险评估和应用程序的安全等级需求，应用程序可以被验证为符合MASVS L1或者L2。L1适用于所有移动应用程序，而L2通常建议用于处理更敏感数据或功能的应用程序。 MASVS-R（或其中的一部分）可以用于验证应用程序抵抗特定威胁的韧性。例如：重新封装或提取敏感数据。*另外*，也可以被用于更严谨的安全验证。

总而言之，可以使用如下的验证类别组合：

- MASVS-L1
- MASVS-L1+R
- MASVS-L2
- MASVS-L2+R

不同的验证类别组合反映出不同的安全等级和弹性。这样的组合方式是为了让安全具有灵活性，例如：手机移动游戏程序出于可用性的需求，可能不需要加入MASVS-L2的安全控制机制，如：双因子身份验证，但是在防篡改方面会存在强烈的业务需求。

#### 如何选择安全验证等级和类型

实现MASVS L2的安全准则可以增加安全性，但是也会增加开发成本，并有可能降低最终用户的体验，这是一种普遍存在的权衡。一般来说，是否采用L2来开发应用程序，要考虑风险与成本(比如，当机密性或完整性被破坏所造成的潜在损失高于额外的安全管控机制的成本时，就应该使用L2)。总体来说，在应用MASVS之前，风险评估应该是第一步。

##### 举例

###### MASVS-L1

- 应用于所有的移动应用程序。MASVS-L1列举了在不过分影响开发成本以及用户体验下的最佳安全实践方法。任何不适用于更严格安全等级的移动应用程序应该采用MASVS-L1标准。

###### MASVS-L2

- 医疗保健行业：存储个人身份信息的移动应用程序，因为这些信息可被用于身份盗窃，诈骗钱财或者其他的欺骗行为，所以应采用MASVS-L2。对于美国的医疗保健行业，需要遵守相关的信息保密法规 - 《健康保险可移植性和责任法案》（HIPAA）中的隐私权，安全性，违约通知规则和患者安全规则。

- 金融行业：可以访问和处理高度敏感信息（例如：信用卡卡号，个人信息或者转账功能）的移动应用程序。这些移动应用程序需要有额外的安全控制措施来防止欺诈行为。金融业相关的应用程序需确保遵守支付卡行业数据安全标准（PCI DSS），《格莱姆·里奇·布利利法案》和《萨班斯-奥克斯利法案》（SOX）。

###### MASVS L1+R

- 以知识产权（IP）保护为商业目标的移动应用程序。MASVS-R中列举的韧性控制可以用于增加攻击者获取源代码，篡改以及破解的难度。

- 游戏行业：游戏应用程序对于防篡改和作弊有着强烈的需求，例如在线竞技游戏。游戏作弊对于在线游戏来说，是一个至关重要的问题，因为大量作弊者的存在，会导致其他玩家的不满，并且最终导致整个游戏的失败。MASVS-R提供了基础的防篡改控件，从而增加游戏作弊者的工作量。

###### MASVS L2+R

- 金融产业：允许用户执行转账操作的手机银行应用程序，存在代码注入和在被不安全设备中运行的风险。在这种情况下，可以使用MASVS-R的安全管控机制了来防止篡改，从而提高恶意程序开发者的门槛。

- 所有在移动设备中需要存储敏感数据，以及支持不同种类的移动设备和操作系统的移动应用程序，建议采用MASVS L2+R。在这种情况下，安全控制机制可以被用来提高纵深防御，从而增加攻击者提取机密数据的难度。

- 带有内购功能的程序，建议采用服务端和MASVS L2来保护付费内容。但是，在某些情况下，无法使用服务端保护。在这些情况下，应该使用MASVS-R来增加逆向和篡改的难度。
