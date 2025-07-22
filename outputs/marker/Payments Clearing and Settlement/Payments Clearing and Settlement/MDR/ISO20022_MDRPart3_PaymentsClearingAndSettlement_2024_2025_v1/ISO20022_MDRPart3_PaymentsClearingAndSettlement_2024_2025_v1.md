## **Introduction**

|                                                                                                                                                            |                |                                                                                                                                                                         |  |  |  | Introduction |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--------------|--|
|                                                                                                                                                            |                |                                                                                                                                                                         |  |  |  |              |  |
| This document describes the Business<br>Model Components and Elements used by<br>the Payments Clearing and Settlement<br>message definitions.              |                |                                                                                                                                                                         |  |  |  |              |  |
|                                                                                                                                                            |                |                                                                                                                                                                         |  |  |  |              |  |
| In the "Business Model" tab, the cells with<br>text in green indicate the business concepts<br>used by the Payments Clearing and<br>Settlement message set |                |                                                                                                                                                                         |  |  |  |              |  |
|                                                                                                                                                            |                |                                                                                                                                                                         |  |  |  |              |  |
| The "Traces" tab shows to which business<br>concepts the Payments Clearing and<br>Settlement message components and<br>message elements trace.             |                |                                                                                                                                                                         |  |  |  |              |  |
|                                                                                                                                                            |                |                                                                                                                                                                         |  |  |  |              |  |
| Notes:                                                                                                                                                     |                |                                                                                                                                                                         |  |  |  |              |  |
|                                                                                                                                                            | Specialisation | Some components inherit from a parent. In this<br>illustration, the AccountContract is a specialisation<br>(a child) of Contract and inherits from all its<br>elements. |  |  |  |              |  |
|                                                                                                                                                            |                | CashAccountContract inherits AccountContract and<br>indirectly from Contract.                                                                                           |  |  |  |              |  |

## **FullBusinessModel**

| Business Component Name | Business Element Name     | Business Component Parent Name |
|-------------------------|---------------------------|--------------------------------|
| ATMTotal                |                           |                                |
| ATMTotal                | ATMBalance                |                                |
| ATMTotal                | Currency                  |                                |
| ATMTotal                | ATMCurrentNumber          |                                |
| ATMTotal                | ATMBalanceNumber          |                                |
| ATMTotal                | ATMCurrent                |                                |
| ATMTotal                | RelatedCardPayment        |                                |
| AcceptorConfiguration   |                           |                                |
| AcceptorConfiguration   | ApplicationIdentification |                                |
| AcceptorConfiguration   | FinancialCapture          |                                |
| AcceptorConfiguration   | BatchTransferContent      |                                |
|                         |                           |                                |

| AcceptorConfiguration | ExchangePolicy           |                      |
|-----------------------|--------------------------|----------------------|
| AcceptorConfiguration | MaximumNumber            |                      |
| AcceptorConfiguration | MaximumAmount            |                      |
| AcceptorConfiguration | ReconciliationByAcquirer |                      |
| AcceptorConfiguration | TotalsPerCurrency        |                      |
| AcceptorConfiguration | ProtectCardData          |                      |
| AcceptorConfiguration | RetailerParameters       |                      |
| AcceptorConfiguration | ApplicationParameters    |                      |
| AcceptorConfiguration | TerminalManagementSystem |                      |
| AcceptorConfiguration | ApplicationVersion       |                      |
| AcceptorRole          |                          | CardPaymentPartyRole |

| Account |                                      |  |
|---------|--------------------------------------|--|
| Account | BaseCurrency                         |  |
| Account | Identification                       |  |
| Account | ParentAccount                        |  |
| Account | SubAccount                           |  |
| Account | RelatedFundProcessingCharacteristics |  |
| Account | Status                               |  |
| Account | Language                             |  |
| Account | PartyRole                            |  |
| Account | TradePartyRole                       |  |

| Account | ReportingCurrency        |  |
|---------|--------------------------|--|
| Account | AccountRestriction       |  |
| Account | SettlementPartyRole      |  |
| Account | Purpose                  |  |
| Account | ClosingDate              |  |
| Account | LiveDate                 |  |
| Account | ReportedPeriod           |  |
| Account | InvestmentFundPartyRole  |  |
| Account | RelatedCollateralProcess |  |
| Account | Type                     |  |
| Account | RelatedProceedsDelivery  |  |
|         |                          |  |

| Account | RelatedCorporateActionPartyRole |  |
|---------|---------------------------------|--|
| Account | DefaultFundAccountOwner         |  |
| Account | System                          |  |
| Account | Balance                         |  |
| Account | Entry                           |  |
| Account | AccountContract                 |  |
| Account | OpeningDate                     |  |
| Account | CurrencyExchange                |  |
| Account | DefaultFundContribution         |  |
| Account | SystemMember                    |  |
|         |                                 |  |

| Account |                 | CollateralAccountType |          |
|---------|-----------------|-----------------------|----------|
| Account |                 | AccountService        |          |
| Account |                 | Reconciliation        |          |
| Account |                 | ManagedAccountProduct |          |
|         | AccountContract |                       | Contract |
|         | AccountContract | TargetClosingDate     |          |
|         | AccountContract | UrgencyFlag           |          |
|         | AccountContract | RemovalIndicator      |          |
|         | AccountContract | TargetGoLiveDate      |          |
|         |                 |                       |          |

| AccountContract       | AccountService       |                  |
|-----------------------|----------------------|------------------|
| AccountContract       | Account              |                  |
| AccountContract       | Interest             |                  |
| AccountContract       | RequestDate          |                  |
| AccountContract       | AccountAuthorisation |                  |
| AccountContract       | TransactionChannel   |                  |
| AccountEntry          |                      | CreditInstrument |
| AccountIdentification |                      |                  |
| AccountIdentification | Account              |                  |
|                       |                      |                  |

| AccountIdentification | IBAN                      |  |
|-----------------------|---------------------------|--|
| AccountIdentification | BBAN                      |  |
| AccountIdentification | UPIC                      |  |
| AccountIdentification | ProprietaryIdentification |  |

| AccountLink             | MarketInfrastructure       |                  |
|-------------------------|----------------------------|------------------|
| AccountLink             | CashSettlementIndicator    |                  |
| AccountLink             | CollateralisationIndicator |                  |
| AccountLink             | DefaultIndicator           |                  |
| AccountOwnerRole        |                            | AccountPartyRole |
| AccountPartyRole        |                            | Role             |
| AccountPartyRole        | Account                    |                  |
| AccountReportedMovement |                            |                  |
|                         |                            |                  |

| AccountReportedMovement     | MonthlyPaymentValue      |                  |
|-----------------------------|--------------------------|------------------|
| AccountReportedMovement     | MonthlyReceivedValue     |                  |
| AccountReportedMovement     | MonthlyTransactionNumber |                  |
| AccountReportedMovement     | AverageBalance           |                  |
| AccountReportedMovement     | ReportedCashAccount      |                  |
| AccountResponsiblePartyRole | AccountPartyRole         |                  |
| AccountRestriction          |                          |                  |
| AccountRestriction          | Account                  |                  |
| AccountRestriction          | RestrictionType          |                  |
| AccountRestriction          | ValidityPeriod           |                  |
| AccountService              |                          | FinancialService |

| AccountService<br>AccountContract<br>AccountService<br>Reservation<br>AccountService<br>Account<br>AccountService<br>AccountAdministrationCharge<br>AccountServicerRole<br>AccountPartyRole<br>AccountServicerRole<br>RelatedPTRR<br>AccountStatus<br>Status<br>AccountStatus<br>Account<br>AccountStatus<br>Status<br>AccountStatus<br>Blocked |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                 |  |  |

| AccountStatus    | ManagementStatus       |                    |
|------------------|------------------------|--------------------|
| AccountStatus    | EntryStatus            |                    |
| AccountStatus    | BalanceStatus          |                    |
| AccountStatus    | BlockedReason          |                    |
| AccountSwitching |                        | CashAccountService |
| AccountSwitching | SwitchReceivedDateTime |                    |
| AccountSwitching | SwitchDate             |                    |
| AccountSwitching | SwitchStatus           |                    |
| AccountSwitching | UniqueReferenceNumber  |                    |
|                  |                        |                    |

| AccountSwitching  | SwitchType            |                          |
|-------------------|-----------------------|--------------------------|
| AccountSwitching  | BalanceTransferWindow |                          |
| AccountingAgent   |                       | SecuritiesTradePartyRole |
| AcquirerRole      |                       | CardPaymentPartyRole     |
| ActivationService |                       |                          |
| ActivationService | DedicatedActivation   |                          |
| ActivationService | EndDate               |                          |
| ActivationService | StartDate             |                          |
| ActivationService | OriginalActivation    |                          |
| ActivationService | RelatedActivation     |                          |
|                   |                       |                          |

| ActivationService       | RelatedElectronicInvoiceProcessingService |  |
|-------------------------|-------------------------------------------|--|
| AdditionalLEIAttributes |                                           |  |
| AdditionalLEIAttributes | RelationshipType                          |  |
| AdditionalLEIAttributes | RelationshipStatus                        |  |
| AdditionalLEIAttributes | RelatedOrganisationIdentification         |  |
| AdditionalLEIAttributes | ManagingLOU                               |  |
| AdditionalRight         |                                           |  |
| AdditionalRight         | Meeting                                   |  |
| AdditionalRight         | Type                                      |  |
|                         |                                           |  |

| AdditionalRight         | AdditionalRightThreshold           |                 |
|-------------------------|------------------------------------|-----------------|
| AdditionalRight         | AdditionalRightThresholdPercentage |                 |
| AdditionalRightDeadline |                                    | MeetingDeadline |
| Adjustment              |                                    |                 |
| Adjustment              | Amount                             |                 |
| Adjustment              | ChargeRate                         |                 |
| Adjustment              | CalculationMethod                  |                 |

| Adjustment | Payment                  |  |
|------------|--------------------------|--|
| Adjustment | Direction                |  |
| Adjustment | Reason                   |  |
| Adjustment | RelatedLineItem          |  |
| Adjustment | AllowanceChargeIndicator |  |
| Adjustment | Price                    |  |
| Adjustment | ChargeIndicator          |  |
| Adjustment | Type                     |  |
| Adjustment | CollateralManagement     |  |
| Adjustment | AdjustedBalance          |  |

| Adjustment         | ChargesPartyRole |                            |
|--------------------|------------------|----------------------------|
| Adjustment         | EffectivePeriod  |                            |
| Adjustment         | CurrencyExchange |                            |
| Adjustment         | SecuritiesOrder  |                            |
| Adjustment         | Tax              |                            |
| AdministratorRole  |                  | InvestmentAccountPartyRole |
| AffirmingPartyRole |                  | SecuritiesTradePartyRole   |

| AgentCorporateActionStandingInstruction |                             | StandingSettlementInstruction |
|-----------------------------------------|-----------------------------|-------------------------------|
| AgentCorporateActionStandingInstruction | StandingInstructionType     |                               |
| AgentCorporateActionStandingInstruction | GrossOrNetIndicator         |                               |
| AgentCorporateActionStandingInstruction | RelatedDeliveryInstructions |                               |
| AgentCorporateActionStandingInstruction | Security                    |                               |
| Agreement                               |                             |                               |
| Agreement                               | DateSigned                  |                               |
| Agreement                               | Description                 |                               |
| Agreement                               | Version                     |                               |
| Agreement                               | ValidityPeriod              |                               |
|                                         |                             |                               |

| Agreement  | Document           |  |
|------------|--------------------|--|
| Agreement  | Trade              |  |
| Agreement  | Jurisdiction       |  |
| Allocation |                    |  |
| Allocation | Percentage         |  |
| Allocation | AllocatedQuantity  |  |
| Allocation | SettlementCurrency |  |
| Allocation | AllocationAccount  |  |
| Allocation | AllocatedPrice     |  |
| Allocation | AllocationAmount   |  |

| Allocation             | Method                        |                |
|------------------------|-------------------------------|----------------|
| Allocation             | AveragePricePrecision         |                |
| Allocation             | SettlementExecutionParameters |                |
| Allocation             | SecuritiesOrder               |                |
| Allocation             | SecuritiesTrade               |                |
| Allocation             | Identification                |                |
| AllocationPartyRole    |                               | TradePartyRole |
| Allowance              |                               | Adjustment     |
| Allowance              | TotalAllowance                |                |
| Allowance              | NetPriceAllowance             |                |
| AmendmentOfUndertaking |                               |                |
| AmendmentOfUndertaking | DateOfIssuance                |                |
| AmendmentOfUndertaking | ChangeOfAmount                |                |
|                        |                               |                |

| AmendmentOfUndertaking | Undertaking                        |  |
|------------------------|------------------------------------|--|
| AmendmentOfUndertaking | BeneficiaryConsentRequestIndicator |  |
| AmendmentOfUndertaking | AmendmentIdentification            |  |
| AmountAndPeriod        |                                    |  |
| AmountAndPeriod        | Period                             |  |
| AmountAndPeriod        | Amount                             |  |
| AmountAndPrice         |                                    |  |
| AmountAndPrice         | Amount                             |  |
| AmountAndPrice         | Price                              |  |
| AmountAndQuantity      |                                    |  |
| AmountAndQuantity      | SecuritiesPricing                  |  |
| AmountAndQuantity      | Amount                             |  |
| AmountAndQuantity      | Quantity                           |  |
| AmountRange            |                                    |  |
| AmountRange            | FromAmount                         |  |
|                        |                                    |  |

| AmountRange         | ToAmount             |  |
|---------------------|----------------------|--|
| AmountRange         | EqualAmount          |  |
| AmountRange         | NotEqualAmount       |  |
| AmountRange         | CreditDebitIndicator |  |
| AmountRange         | Currency             |  |
| AmountRange         | RelatedInterest      |  |
| AmountRangeBoundary |                      |  |
| AmountRangeBoundary | FromAmountRange      |  |
| AmountRangeBoundary | BoundaryAmount       |  |
| AmountRangeBoundary | Included             |  |
| AmountRangeBoundary | ToAmountRange        |  |
| AmountRatio         |                      |  |
| AmountRatio         | SecuritiesPricing    |  |
| AmountRatio         | Amount1              |  |
|                     |                      |  |

| AmountRatio          | Amount2               |  |
|----------------------|-----------------------|--|
| AnalyticsCalculation |                       |  |
| AnalyticsCalculation | SecuritiesPricing     |  |
| AnalyticsCalculation | Value                 |  |
| AnalyticsCalculation | CalculationType       |  |
| AnalyticsCalculation | ValueDate             |  |
| AnalyticsCalculation | ValuePeriod           |  |
| AnalyticsCalculation | EstimatedInterestRate |  |
| AnalyticsCalculation | VariableRateValueDate |  |
| AnalyticsValue       |                       |  |
| AnalyticsValue       | Amount                |  |
| AnalyticsValue       | Rate                  |  |
|                      |                       |  |

| AnalyticsValue | NumberOfYears        |          |
|----------------|----------------------|----------|
| AnalyticsValue | AnalyticsCalculation |          |
| Assessment     |                      | Document |
| Assessment     | AssessmentType       |          |
| Assessment     | System               |          |
| Assessment     | ExpiryDate           |          |
| Assessment     | DeliveryDate         |          |
| Asset          |                      |          |
| Asset          | ExpiryDate           |          |
| Asset          | MaturityDate         |          |
| Asset          | Derivative           |          |

| Asset | AssetValue                      |
|-------|---------------------------------|
| Asset | AssetClassification             |
| Asset | FinancialAssetCategory          |
| Asset | AssetPartyRole                  |
| Asset | Issuance                        |
| Asset | Portfolio                       |
| Asset | InvestmentAmount                |
| Asset | InvestmentRate                  |
| Asset | EffectiveDate                   |
| Asset | FinancialInstrumentSubStructure |
| Asset | InvestmentPlan                  |
| Asset | Trade                           |
| Asset | Tranche                         |
| Asset | LegAdditionalInformation        |

| Asset               | StandingSettlementInstruction |                   |
|---------------------|-------------------------------|-------------------|
| Asset               | GenericAssetIdentification    |                   |
| AssetClassStrategy  |                               | PortfolioStrategy |
| AssetClassStrategy  | AssetClass                    |                   |
| AssetClassification |                               |                   |
| AssetClassification | ClassificationType            |                   |
| AssetClassification | Asset                         |                   |
| AssetClassification | Language                      |                   |
| AssetClassification | AssetClassScheme              |                   |
| AssetClassification | ProductType                   |                   |
| AssetClassification | Strategy                      |                   |
| AssetClassification | ClassificationSubType         |                   |

| AssetHolding<br>AssetHolding<br>HoldingValue<br>AssetHolding<br>BookValue<br>AssetHolding<br>FaceAmount<br>AssetHolding<br>AmortisedFaceValue<br>AssetHolding<br>MarketValue<br>AssetHolding<br>Balance<br>AssetHolding<br>UnrealisedGainOrLoss<br>AssetHolding<br>Asset |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                          |  |  |

| AssetHolding | Haircut                 |  |
|--------------|-------------------------|--|
| AssetHolding | EligibleCollateralValue |  |
| AssetHolding | ExchangeRate            |  |
| AssetHolding | CapValue                |  |
| AssetHolding | RiskAdjustedValue       |  |
| AssetHolding | RealisedGainOrLoss      |  |
| AssetHolding | UnrealisedType          |  |
| AssetHolding | PostHaircutValue        |  |

| AssetHolding   | Interest                    |      |
|----------------|-----------------------------|------|
| AssetHolding   | Collateral                  |      |
| AssetHolding   | FinancialAssetType          |      |
| AssetHolding   | VariationMarginCollateral   |      |
| AssetHolding   | IndependentAmountCollateral |      |
| AssetHolding   | HoldingType                 |      |
| AssetHolding   | GuaranteeAmount             |      |
| AssetPartyRole |                             | Role |
| AssetPartyRole | Asset                       |      |
|                |                             |      |

| AssignedProxyRole |                      | MeetingPartyRole       |
|-------------------|----------------------|------------------------|
| AssignedProxyRole | ProxyPerson          |                        |
| AssignedProxyRole | PreAssignedProxyRole |                        |
| Assignee          |                      | InvestigationPartyRole |
| Assigner          |                      | InvestigationPartyRole |
| Assignment        |                      |                        |
| Assignment        | PaymentObligation    |                        |
| Assignment        | FinancingAgreement   |                        |
| Assured           |                      | InsurancePartyRole     |
| Assured           | AssuredType          |                        |

| AttendanceCard                 |                         |                         |
|--------------------------------|-------------------------|-------------------------|
| AttendanceCard                 | AttendanceCardLabelling |                         |
| AttendanceCard                 | MeetingAttendance       |                         |
| AttendanceCard                 | DeliveryMethod          |                         |
| AttendanceCard                 | DeliveryPlace           |                         |
| AttendanceConfirmationDeadline |                         | MeetingDeadline         |
| Auditor                        |                         | InvestmentFundPartyRole |

| AustralianBSBIdentification |                                        |  |
|-----------------------------|----------------------------------------|--|
| AustralianBSBIdentification | ExtensiveBranchNetworkIdentification   |  |
| AustralianBSBIdentification | SmallNetworkIdentification             |  |
| AustralianBSBIdentification | ClearingSystemMemberIdentificationType |  |
| AustralianBSBIdentification | ClearingSystemMember                   |  |
| Authentication              |                                        |  |
| Authentication              | Cardholder                             |  |
| Authentication              | AuthenticationMethod                   |  |
|                             |                                        |  |

| Authentication            | AuthenticationEntity  |                      |
|---------------------------|-----------------------|----------------------|
| Authentication            | AuthenticationValue   |                      |
| Authentication            | PINFormat             |                      |
| Authentication            | PIN                   |                      |
| Authentication            | AuthenticationSupport |                      |
| Authentication            | CollectionIndicator   |                      |
| Authentication            | Mandate               |                      |
| Authentication            | AuthenticationResult  |                      |
| Authentication            | Exemption             |                      |
| AuthorisationEntity       |                       | CardPaymentPartyRole |
| AuthorisedAccountModifier |                       | AccountPartyRole     |
|                           |                       |                      |

| AutomaticVariation |                      |  |
|--------------------|----------------------|--|
| AutomaticVariation | Undertaking          |  |
| AutomaticVariation | Type                 |  |
| AutomaticVariation | VariationAmount      |  |
| AutomaticVariation | Trigger              |  |
| Balance            |                      |  |
| Balance            | Type                 |  |
| Balance            | ValueDate            |  |
| Balance            | CreditDebitIndicator |  |
| Balance            | AssetHolding         |  |
| Balance            | CalculationDate      |  |
|                    |                      |  |

| Balance         | Adjustment            |                    |
|-----------------|-----------------------|--------------------|
| Balance         | Account               |                    |
| Balance         | Interest              |                    |
| Balance         | BalanceEntry          |                    |
| Balance         | ProcessingRestriction |                    |
| Balance         | OpeningClosingCode    |                    |
|                 |                       |                    |
| BankOperation   |                       | CashAccountService |
| BankOperation   | OperationThreshold    |                    |
| BankOperation   | OperationType         |                    |
| BankOperation   | ApplicablePeriod      |                    |
| BankTransaction |                       |                    |
| BankTransaction | Domain                |                    |

| BankTransaction    | Family                    |  |
|--------------------|---------------------------|--|
| BankTransaction    | SubFamily                 |  |
| BankTransaction    | ProprietaryIdentification |  |
| BankTransaction    | BankOperation             |  |
| BankTransaction    | RelatedEntry              |  |
| BankTransaction    | RelatedPayment            |  |
| BankingTransaction |                           |  |
| BankingTransaction | PaymentObligation         |  |
| BankingTransaction | FinancialTransaction      |  |
| BankingTransaction | CashDelivery              |  |
| BankingTransaction | CashDeposit               |  |
|                    |                           |  |

| BaselineStatus              |                             | Status              |
|-----------------------------|-----------------------------|---------------------|
| BaselineStatus              | Status                      |                     |
| BaselineStatus              | CommercialTrade             |                     |
| BasicSecuritiesRegistration |                             |                     |
| BasicSecuritiesRegistration | Security                    |                     |
| BasicSecuritiesRegistration | RegistrationInstruction     |                     |
| BasicSecuritiesRegistration | CertificationIdentification |                     |
| BasicSecuritiesRegistration | CertificationDate           |                     |
| BasicSecuritiesRegistration | SecuritiesCertificate       |                     |
| BasicSecuritiesRegistration | SplitPeriod                 |                     |
| BeneficialOwner             |                             | SecuritiesPartyRole |
| BeneficialOwner             | CertificationType           |                     |

| BeneficialOwner<br>NonDomicileCountry<br>BeneficialOwner<br>CertificationIndicator<br>BeneficialOwner<br>CertificationFormat<br>BeneficialOwner<br>ERISAEligibility<br>BeneficialOwner<br>ERISARate<br>BeneficialOwner<br>BenefitPlanDeclarationIndicator<br>BiddingConditions<br>BiddingConditions<br>ProposedRate<br>BiddingConditions<br>OversubscriptionRate |  |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                  |  |  |

| BiddingConditions | InformationToComplyWith        |  |
|-------------------|--------------------------------|--|
| BiddingConditions | SubscriptionCostDebitDate      |  |
| BiddingConditions | MaximumAllowedOverSubscription |  |
| BiddingConditions | ProrationRate                  |  |
| BiddingConditions | ApplicableRate                 |  |
| BiddingConditions | FrontEndOddLotQuantity         |  |
| BiddingConditions | BackEndOddLotQuantity          |  |
|                   |                                |  |

| BiddingConditions<br>TransformationRate       |
|-----------------------------------------------|
| BiddingConditions<br>ProrationDate            |
| BiddingConditions<br>CompulsoryPurchasePeriod |
| BiddingConditions<br>PercentageSought         |
| BiddingConditions<br>BidInterval              |
| BiddingConditions<br>MaximumPrice             |
| BiddingConditions<br>MinimumPrice             |
| BiddingConditions<br>MaximumQuantity          |

| BiddingConditions<br>MinimumQuantitySought      |
|-------------------------------------------------|
|                                                 |
| BiddingConditions<br>BaseDenomination           |
| BiddingConditions<br>CalculationMethod          |
| BiddingConditions<br>AdditionalSubscriptionCost |
| BiddingConditions<br>Event                      |
| BillTo<br>CommercialTradePartyRole              |
| BondCounsel<br>SecuritiesPartyRole              |
| BookEntry<br>CreditInstrument                   |
| BookEntry<br>CashEntry                          |

| BookEntry | DebitEntry                   |                |
|-----------|------------------------------|----------------|
| BookEntry | CreditEntry                  |                |
| BookEntry | TransferAdvice               |                |
| BookEntry | FundSubscriptionCashInFlow   |                |
| BookEntry | FundRedemptionCashOutFlow    |                |
| BookEntry | RelatedSettlementInstruction |                |
| Borrower  |                              | TradePartyRole |
| Broker    |                              | TradePartyRole |
| Broker    | RemunerationAmount           |                |
|           |                              |                |

| Broker      | Commission             |                      |
|-------------|------------------------|----------------------|
|             |                        |                      |
| BulkPayment |                        | Payment              |
|             |                        |                      |
| BulkPayment | Groups                 |                      |
|             |                        |                      |
| BuyIn       |                        | ObligationFulfilment |
|             |                        |                      |
| BuyIn       | SecuritiesCompensation |                      |
| BuyIn       | BuyinDate              |                      |
| BuyIn       | BuyInPrice             |                      |
| BuyIn       | Fees                   |                      |

| BuyIn                         | CashCompensation                 |  |
|-------------------------------|----------------------------------|--|
| BuyIn                         | RelatedSecuritiesClearingProcess |  |
| BuyOrSellIndicationOfInterest |                                  |  |
| BuyOrSellIndicationOfInterest | NegotiationDetails               |  |
| BuyOrSellIndicationOfInterest | Organisations                    |  |
| BuyOrSellIndicationOfInterest | RelativeSize                     |  |
| BuyOrSellIndicationOfInterest | Price                            |  |
| BuyOrSellIndicationOfInterest | QualityIndication                |  |
| BuyOrSellIndicationOfInterest | NaturalIndicator                 |  |

| BuyOrSellIndicationOfInterest | Qualifier            |                |
|-------------------------------|----------------------|----------------|
| BuyOrSellIndicationOfInterest | NumberOfLegs         |                |
| BuyOrSellIndicationOfInterest | SpreadToBenchmark    |                |
| BuyOrSellIndicationOfInterest | SwapSpread           |                |
| BuyOrSellIndicationOfInterest | TwoLegTransaction    |                |
| BuyOrSellIndicationOfInterest | RoutingType          |                |
| BuyOrSellIndicationOfInterest | OrganisationListName |                |
| BuyerBank                     |                      | TradePartyRole |
| BuyerRole                     |                      | TradePartyRole |
| CRSStatus                     |                      |                |
| CRSStatus                     | CRSStatus            |                |

| CRSStatus    | ExceptionalReportingCountry | Reporting country for the CRS<br>status when there is an<br>CountryCode<br>exception at the country level.                                                                                |
|--------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CRSStatus    | CRSSourceStatus             | Source of the Common Reporting<br>Standard (CRS) status expressed<br>CRSSourceStatusCode<br>as a code.                                                                                    |
| CRSStatus    | CRSReportingDate            | Date provided by the account<br>owner to inform the account<br>servicer of the date on which the<br>ISODate<br>holdings must be reported before<br>the account is subsequently<br>closed. |
| CRSStatus    | InvestmentAccountParty      | Common Reporting Standard<br>(CRS) status linked to an<br>InvestmentAccountPartyRole<br>investment account and played<br>by a party in that context.                                      |
| Capital      |                             | Amount of money targeted to be<br>raised through the issuance of a<br>security.                                                                                                           |
| Capital      | AssetIssuance               | Issued asset.<br>Issuance                                                                                                                                                                 |
| Capital      | Date                        | Date/time at which capital<br>ISODateTime<br>amount was recorded.                                                                                                                         |
| Capital      | Type                        | Specifies the type of capital.<br>CapitalTypeCode                                                                                                                                         |
| Capital      | Amount                      | Capital expressed as a currency<br>CurrencyAndAmount<br>and amount.                                                                                                                       |
| Capital      | Unit                        | Capital expressed as a number of<br>DecimalNumber<br>units.                                                                                                                               |
| CapitalValue |                             | Value of the capital.                                                                                                                                                                     |
|              |                             |                                                                                                                                                                                           |

| CapitalValue | Capital                  |                      |
|--------------|--------------------------|----------------------|
| CappedLimit  |                          |                      |
| CappedLimit  | IncomeCurrentPeriod      |                      |
| CappedLimit  | StartDate                |                      |
| CappedLimit  | IncomeLimitCurrentPeriod |                      |
| CappedLimit  | RelatedDrawdown          |                      |
| CappedLimit  | IncomeLimitNextPeriod    |                      |
| CardIssuer   |                          | CardPaymentPartyRole |
| CardPayment  |                          | IndividualPayment    |
| CardPayment  | PaymentCard              |                      |
| CardPayment  | Product                  |                      |
| CardPayment  | DetailedAmount           |                      |
| CardPayment  | AmountQualifier          |                      |
| CardPayment  | CardPaymentAcquiring     |                      |
|              |                          |                      |

| CardPayment          | PaymentCardPartyRole      |  |
|----------------------|---------------------------|--|
| CardPayment          | CardPaymentStatus         |  |
| CardPayment          | DetailedAmountLabel       |  |
| CardPayment          | Reconciliation            |  |
| CardPayment          | TransactionCategory       |  |
| CardPayment          | CashBackAmount            |  |
| CardPayment          | Gratuity                  |  |
| CardPayment          | DebitCreditDirection      |  |
| CardPayment          | ATMTotal                  |  |
| CardPaymentAcquiring |                           |  |
| CardPaymentAcquiring | PointOfInteraction        |  |
| CardPaymentAcquiring | CardPaymentService        |  |
| CardPaymentAcquiring | TransactionIdentification |  |

| CardPaymentAcquiring | TransactionDateTime     |  |
|----------------------|-------------------------|--|
| CardPaymentAcquiring | ICCRelatedData          |  |
| CardPaymentAcquiring | RelatedCardPayment      |  |
| CardPaymentAcquiring | CardPresent             |  |
| CardPaymentAcquiring | CardholderPresent       |  |
| CardPaymentAcquiring | OnLineContext           |  |
| CardPaymentAcquiring | AttendanceContext       |  |
| CardPaymentAcquiring | TransactionEnvironment  |  |
| CardPaymentAcquiring | TransactionChannel      |  |
| CardPaymentAcquiring | AttendantMessageCapable |  |
| CardPaymentAcquiring | AttendantLanguage       |  |
|                      |                         |  |

| CardPaymentAcquiring | CardDataEntryMode              |  |
|----------------------|--------------------------------|--|
| CardPaymentAcquiring | FallbackIndicator              |  |
| CardPaymentAcquiring | TMSTrigger                     |  |
| CardPaymentAcquiring | InitiatorTransactionIdentifier |  |
| CardPaymentAcquiring | Reversal                       |  |
| CardPaymentAcquiring | InterchangeData                |  |
| CardPaymentAcquiring | UnattendedLevelCategory        |  |
| CardPaymentAcquiring | Validation                     |  |
| CardPaymentAcquiring | CompletionRequired             |  |
| CardPaymentAcquiring | ActionType                     |  |
|                      |                                |  |

| CardPaymentAcquiring | ActionMessage                      |        |
|----------------------|------------------------------------|--------|
| CardPaymentAcquiring | CaptureIndicator                   |        |
| CardPaymentAcquiring | RecipientTransactionIdentification |        |
| CardPaymentAcquiring | Location                           |        |
| CardPaymentAcquiring | Country                            |        |
| CardPaymentAcquiring | ReSubmissionCounter                |        |
| CardPaymentAcquiring | BusinessArea                       |        |
| CardPaymentPartyRole |                                    | Role   |
| CardPaymentPartyRole | CardPayment                        |        |
| CardPaymentPartyRole | PartyType                          |        |
| CardPaymentStatus    |                                    | Status |

| CardPaymentStatus     | RejectionReason    |  |
|-----------------------|--------------------|--|
| CardPaymentStatus     | FailureReason      |  |
| CardPaymentStatus     | CardPayment        |  |
| CardPaymentValidation |                    |  |
| CardPaymentValidation | TransactionSuccess |  |
| CardPaymentValidation | MerchantOverride   |  |
| CardPaymentValidation | ValidityDate       |  |
| CardPaymentValidation | CardPayment        |  |
| CardPaymentValidation | Response           |  |
| CardPaymentValidation | AuthorisationCode  |  |
| CardPaymentValidation | OnLineReason       |  |
| CardPaymentValidation | Balance            |  |
|                       |                    |  |

| CardPaymentValidation | CardholderAddressVerificationResult    |                        |
|-----------------------|----------------------------------------|------------------------|
| CardPaymentValidation | CSCResult                              |                        |
| CardPaymentValidation | DeclinedProductCode                    |                        |
| CardPaymentValidation | ElectronicCommerceAuthenticationResult |                        |
| CardPaymentValidation | FailureReason                          |                        |
| CardPaymentValidation | Signature                              |                        |
| CardholderRole        |                                        | CardPaymentPartyRole   |
| CardholderRole        | Authentication                         |                        |
| Carrier               |                                        | TransportPartyRole     |
| CarrierAgent          |                                        | TransportPartyRole     |
| CaseCreator           |                                        | InvestigationPartyRole |

| CashAccount<br>Account<br>CashAccount<br>CashAccountType<br>CashAccount<br>RelatedInvestmentAccount<br>CashAccount<br>CashEntry<br>CashAccount<br>CashBalance<br>CashAccount<br>PaymentPartyRole<br>CashAccount<br>RelatedCreditStandingOrder<br>CashAccount<br>RelatedDebitStandingOrder<br>CashAccount<br>CashAccountContract |  |  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                 |  |  |

| CashAccount | RelatedCorporateActionElection   | Election process which uses<br>specific cash accounts.                                                                |
|-------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| CashAccount | Charges                          | Specifies the charges which are<br>debited from the account.                                                          |
| CashAccount | Tax                              | Tax charged on a cash account.                                                                                        |
| CashAccount | RelatedSettlementInstruction     | Settlement process which uses<br>specific cash accounts.                                                              |
| CashAccount | CashSettlementPartyRole          | Specifies each role linked to a<br>payment settlement and using a<br>specific cash account in the<br>payment context. |
| CashAccount | UltimateObligor                  | Party for which different types of<br>cash accounts are specified.                                                    |
| CashAccount | RelatedPaymentCard               | Payment card for which an<br>account is specified.                                                                    |
| CashAccount | SecuritiesPartyRole              | Specifies the role which uses a<br>cash account.                                                                      |
| CashAccount | RelatedInvoiceFinancingPartyRole | Specifies each role using a<br>specific account in the context of<br>invoice financing.                               |
| CashAccount | RelatedCommercialTrade           | Commercial trade for which a<br>purchase account is specified.                                                        |
| CashAccount | Level                            | Defines the level of an account<br>within the account hierarchy.                                                      |
| CashAccount | SettlementCurrency               | Specifies the currency used for<br>settlement, if different from the<br>account currency.                             |

| CashAccount         | ReportedMovements     |                 |
|---------------------|-----------------------|-----------------|
| CashAccount         | ClosedAccountContract |                 |
| CashAccount         | AccountLink           |                 |
| CashAccount         | CashStandingOrder     |                 |
| CashAccount         | Cheque                |                 |
| CashAccount         | CashAccountService    |                 |
| CashAccount         | Payment               |                 |
| CashAccount         | Commission            |                 |
| CashAccountContract |                       | AccountContract |
|                     |                       |                 |

| CashAccountContract | CashAccount         |         |
|---------------------|---------------------|---------|
| CashAccountContract | TransferCashAccount |         |
| CashAccountContract | Services            |         |
| CashAccountContract | BalanceTransfer     |         |
| CashAccountContract | CashAccountMandate  |         |
| CashAccountMandate  |                     | Mandate |
| CashAccountMandate  | Services            |         |
| CashAccountMandate  | CashAccountContract |         |

| CashAccountService |                     | AccountService |
|--------------------|---------------------|----------------|
| CashAccountService | CashAccountMandate  |                |
| CashAccountService | CompensationMethod  |                |
| CashAccountService | BillingCurrency     |                |
| CashAccountService | BillingChargeMethod |                |
| CashAccountService | PaymentMethod       |                |
| CashAccountService | CashAccountContract |                |
| CashAccountService | Identification      |                |
| CashAccountService | CashAccount         |                |
|                    |                     |                |

| CashAvailability |                      |         |
|------------------|----------------------|---------|
| CashAvailability | CashBalance          |         |
| CashAvailability | Date                 |         |
| CashAvailability | NumberOfDays         |         |
| CashAvailability | Amount               |         |
| CashAvailability | CashEntry            |         |
| CashAvailability | CreditDebitIndicator |         |
| CashBalance      |                      | Balance |
| CashBalance      | CashAccount          |         |
| CashBalance      | CalculationType      |         |

| CashBalance | Counterparty                        |  |
|-------------|-------------------------------------|--|
| CashBalance | Amount                              |  |
| CashBalance | Availability                        |  |
| CashBalance | CashBalanceEntry                    |  |
| CashBalance | BalanceAdjustmentCode               |  |
| CashBalance | RelatedCardPaymentValidationProcess |  |
| CashBalance | CutOffDate                          |  |
| CashBalance | RelatedRegisteredContract           |  |

| CashClearingSystem       |                            | ClearingSystem |
|--------------------------|----------------------------|----------------|
| CashClearingSystem       | Identification             |                |
| CashClearingSystem       | TransactionAdministrator   |                |
| CashClearingSystem       | SystemRole                 |                |
| CashClearingSystem       | Type                       |                |
| CashClearingSystem       | CashSettlementSystem       |                |
| CashClearingSystemMember |                            |                |
| CashClearingSystemMember | OrganisationIdentification |                |
|                          |                            |                |

| CashClearingSystemMember | CHIPSUniversalIdentification |  |
|--------------------------|------------------------------|--|
| CashClearingSystemMember | NewZealandNCC                |  |
| CashClearingSystemMember | IrishNSC                     |  |
| CashClearingSystemMember | UKSortCode                   |  |

| CashClearingSystemMember | CHIPSParticipantIdentification       |  |
|--------------------------|--------------------------------------|--|
| CashClearingSystemMember | SwissBC                              |  |
| CashClearingSystemMember | FedwireRoutingNumber                 |  |
| CashClearingSystemMember | PortugueseNCC                        |  |
| CashClearingSystemMember | RussianCentralBankIdentificationCode |  |
| CashClearingSystemMember | ItalianDomesticIdentificationCode    |  |

| CashClearingSystemMember | AustrianBankleitzahl                     |  |
|--------------------------|------------------------------------------|--|
| CashClearingSystemMember | CanadianPaymentsAssociationRoutingNumber |  |
| CashClearingSystemMember | SwissSIC                                 |  |
| CashClearingSystemMember | GermanBankleitzahl                       |  |
| CashClearingSystemMember | SpanishDomesticInterbankingCode          |  |
| CashClearingSystemMember | SouthAfricanNCC                          |  |

| CashClearingSystemMember | HongKongBankCode               |                  |
|--------------------------|--------------------------------|------------------|
| CashClearingSystemMember | ClearingMember                 |                  |
| CashClearingSystemMember | IndianFinancialSystemCode      |                  |
| CashClearingSystemMember | HellenicBankIdentificationCode |                  |
| CashClearingSystemMember | PolishNationalClearingCode     |                  |
| CashClearingSystemMember | AustralianBSBCode              |                  |
| CashDelivery             |                                | CreditInstrument |
| CashDelivery             | CashAmount                     |                  |

| CashDelivery     | RelatedBankingTransaction               |                   |
|------------------|-----------------------------------------|-------------------|
| CashDeposit      |                                         | IndividualPayment |
| CashDeposit      | NoteDenomination                        |                   |
| CashDeposit      | NumberOfNotes                           |                   |
| CashDeposit      | DepositAmount                           |                   |
| CashDeposit      | RelatedBankingTransaction               |                   |
| CashDistribution |                                         | Distribution      |
| CashDistribution | DistributionCurrencyExchangeInformation |                   |
| CashDistribution | SecuritiesAndCashDistribution           |                   |
| CashDistribution | AmortisedRate                           |                   |
|                  |                                         |                   |

| CashDistribution | Rate                          |  |
|------------------|-------------------------------|--|
| CashDistribution | CashIndemnityRate             |  |
| CashDistribution | DividendReinvestmentIndicator |  |
| CashDistribution | InterestAmount                |  |
| CashDistribution | InterestRate                  |  |
| CashDistribution | LoyaltyPremiumIndicator       |  |
| CashDistribution | PaymentType                   |  |
| CashDistribution | SelectionDate                 |  |
| CashDistribution | CashDistributionRate          |  |

| CashDistribution | CashDistributionAmount |       |
|------------------|------------------------|-------|
| CashEntry        |                        | Entry |
| CashEntry        | CashAccount            |       |
| CashEntry        | Amount                 |       |
| CashEntry        | RelatedBookEntry       |       |
| CashEntry        | CashBalance            |       |
| CashEntry        | CurrencyExchange       |       |
| CashEntry        | Charges                |       |
| CashEntry        | Availability           |       |

| CashEntry             | Interest                           |                    |
|-----------------------|------------------------------------|--------------------|
| CashEntry             | DebitRelatedBookEntry              |                    |
| CashEntry             | CreditRelatedBookEntry             |                    |
| CashEntry             | RelatedInvoiceFinancingTransaction |                    |
| CashEntry             | RelatedInvestigationCase           |                    |
| CashEntry             | RelatedInvestigationCaseResolution |                    |
| CashEntry             | ChargesIncluded                    |                    |
| CashLoanDeposit       |                                    | Deposit            |
| CashManagementService |                                    | CashAccountService |
|                       |                                    |                    |

| CashManagementService | RiskManagementLimit             |  |
|-----------------------|---------------------------------|--|
| CashManagementService | StandingOrder                   |  |
| CashManagementService | RelatedTransactionAdministrator |  |
| CashManagementService | LiquidityManagementLimit        |  |
| CashManagementService | CallInType                      |  |
|                       |                                 |  |

| CashProceedsDefinition |                             | ProceedsDefinition |
|------------------------|-----------------------------|--------------------|
| CashProceedsDefinition | CashIncentiveRate           |                    |
| CashProceedsDefinition | ContractualPaymentIndicator |                    |
| CashProceedsDefinition | IncomeType                  |                    |
| CashProceedsDefinition | IndemnityAmount             |                    |
| CashProceedsDefinition | CashIncentiveAmount         |                    |
| CashProceedsDefinition | PrincipalOrCorpus           |                    |
|                        |                             |                    |

| CashProceedsDefinition | RedemptionPremiumAmount   |            |
|------------------------|---------------------------|------------|
| CashProceedsDefinition | IncomePortion             |            |
| CashProceedsDefinition | Interest                  |            |
| CashProceedsDefinition | Amount                    |            |
| CashProceedsDefinition | Dividend                  |            |
| CashProceedsDefinition | PaymentCurrency           |            |
| CashProceedsDefinition | StatusCashAmount          |            |
| CashProceedsDefinition | PriceCalculationMethod    |            |
| CashSettlement         |                           | Settlement |
| CashSettlement         | InterbankSettlementAmount |            |

| CashSettlement | InterbankSettlementDate         |  |
|----------------|---------------------------------|--|
| CashSettlement | RTGS                            |  |
| CashSettlement | CreditDateTime                  |  |
| CashSettlement | RelatedPaymentInstruction       |  |
| CashSettlement | SettlementMethod                |  |
| CashSettlement | SettlementAccount               |  |
| CashSettlement | DebitDateTime                   |  |
| CashSettlement | PartyRole                       |  |
| CashSettlement | RelatedTransactionAdministrator |  |

| CashSettlement                     | BookEntry                |                     |
|------------------------------------|--------------------------|---------------------|
| CashSettlement                     | RelatedInvestigationCase |                     |
| CashSettlement                     | Reservation              |                     |
| CashSettlementInstructionPartyRole |                          | SettlementPartyRole |
| CashSettlementInstructionPartyRole | CashAccount              |                     |
| CashSettlementInstructionPartyRole | SettlementInstruction    |                     |
| CashStandingOrder                  |                          | StandingOrder       |

| CashStandingOrder | ZeroSweepIndicator   |                      |
|-------------------|----------------------|----------------------|
| CashStandingOrder | RelatedCashServices  |                      |
| CashStandingOrder | CreditDebitIndicator |                      |
| CashStandingOrder | CreditTransfer       |                      |
| CashStandingOrder | FloorAmount          |                      |
| CashStandingOrder | CashAccount          |                      |
| Cashier           |                      | CardPaymentPartyRole |
| Cashier           | ShiftNumber          |                      |

| CentralClearingCounterpartyRole           | SettlementPartyRole |
|-------------------------------------------|---------------------|
| CentralClearingCounterpartyRole<br>System |                     |
| CentralSecuritiesDepositoryRole           | DepositoryRole      |
| ChargeAccountAgent                        | ChargePartyRole     |
| ChargeAgent                               | ChargePartyRole     |
| ChargeBearer                              | ChargePartyRole     |
| ChargePartyRole                           | Role                |

| ChargePartyRole | Adjustment                |                 |
|-----------------|---------------------------|-----------------|
| ChargeRecipient |                           | ChargePartyRole |
| Charges         |                           | Adjustment      |
| Charges         | ChargeType                |                 |
| Charges         | CalculationBasis          |                 |
| Charges         | BearerType                |                 |
| Charges         | ChargesDebitAccount       |                 |
| Charges         | CashEntry                 |                 |
| Charges         | CreditDebitIndicator      |                 |
| Charges         | MaximumAmount             |                 |
| Charges         | InvestmentFundTransaction |                 |
| Charges         | LogisticsChargeLineItem   |                 |

| Charges | Transport              |
|---------|------------------------|
| Charges | Services               |
| Charges | RelatedUndertaking     |
| Charges | LineItem               |
| Charges | NetPriceChargeLineItem |
| Charges | BaseAmount             |
| Charges | MaximumRate            |
| Charges | MinimumRate            |
| Charges | MinimumAmount          |
| Charges | RelatedInterest        |
| Charges | ChargePaymentMethod    |
|         |                        |

| CheckingPartyRole |                      | DocumentPartyRole |
|-------------------|----------------------|-------------------|
| Cheque            |                      | FinancialDocument |
| Cheque            | ChequeDelivery       |                   |
| Cheque            | Number               |                   |
| Cheque            | ChequeType           |                   |
| Cheque            | MaturityDate         |                   |
| Cheque            | FormsCode            |                   |
| Cheque            | MemoField            |                   |
| Cheque            | RegionalClearingZone |                   |
|                   |                      |                   |

| Cheque          | RelatedPayment  |                   |
|-----------------|-----------------|-------------------|
| Cheque          | ChequePartyRole |                   |
| Cheque          | CashAccount     |                   |
| ChequeIssue     |                 | CreditInstrument  |
| ChequeIssue     | Cheque          |                   |
| ChequeIssue     | DeliveryMethod  |                   |
| ChequeIssue     | DeliverTo       |                   |
| ChequeIssue     | PrintLocation   |                   |
| ChequePartyRole |                 | Role              |
| ChequePartyRole | Cheque          |                   |
| ChequePayment   |                 | IndividualPayment |
| ChequePayment   | Cheque          |                   |

| ChoiceCorporateAction |                                 | MandatoryCorporateAction |
|-----------------------|---------------------------------|--------------------------|
| ChoiceCorporateAction | CorporateActionOptionDefinition |                          |
| ClaimsAgent           |                                 | InsurancePartyRole       |
| ClassAction           |                                 |                          |
| ClassAction           | ClassActionNumber               |                          |
| ClassAction           | LeadPlaintiffDeadline           |                          |
| ClassAction           | CourtApprovalDate               |                          |
| ClassAction           | ClaimPeriod                     |                          |
| ClassAction           | FilingDate                      |                          |
|                       |                                 |                          |

| ClassAction | HearingDate                |                      |
|-------------|----------------------------|----------------------|
| ClassAction | CorporateEvent             |                      |
| Clearing    |                            | ObligationFulfilment |
| Clearing    | ClearingThresholdIndicator |                      |
| Clearing    | ClearedIdentification      |                      |
| Clearing    | GuaranteedTrade            |                      |
| Clearing    | TradePostingType           |                      |
|             |                            |                      |

| Clearing                     | ClearingSystem             |                 |
|------------------------------|----------------------------|-----------------|
| ClearingBroker               |                            | Broker          |
| ClearingBrokerIdentification |                            |                 |
| ClearingBrokerIdentification | RelatedTradeIdentification |                 |
| ClearingBrokerIdentification | SideIndicator              |                 |
| ClearingBrokerIdentification | Identification             |                 |
| ClearingExceptionPartyRole   |                            | TradePartyRole  |
| ClearingMemberRole           |                            | SystemPartyRole |

| ClearingMemberRole | ClearingSystemMemberIdentification |  |
|--------------------|------------------------------------|--|
| ClearingMemberRole | Side                               |  |
| ClearingMemberRole | ClearingAccount                    |  |
| ClearingMemberRole | MarginAccount                      |  |
| ClearingMemberRole | DeliveryAccount                    |  |
| ClearingMemberRole | DefaultFundAccount                 |  |
| ClearingMemberRole | ClearingSegment                    |  |

| ClearingMemberRole | RelatedClearingMemberRole   |                     |
|--------------------|-----------------------------|---------------------|
| ClearingPlace      |                             | SettlementPartyRole |
| ClearingSystem     |                             | System              |
| ClearingSystem     | Clearing                    |                     |
| ClearingSystem     | CentralClearingCounterparty |                     |
| ClearingSystem     | DefaultFund                 |                     |
| ClearingSystem     | CollateralManagement        |                     |
| Collateral         |                             |                     |
| Collateral         | CollateralAmount            |                     |

| Collateral<br>Valuation<br>Collateral<br>CollateralType<br>Collateral<br>BaseCurrencyAmount<br>Collateral<br>CollateralPurpose<br>Collateral<br>CollateralBalance<br>Collateral<br>CollateralAccount<br>Collateral<br>CollateralManagement<br>Collateral<br>CollateralPartyRole<br>Collateral<br>Status<br>Collateral<br>AssetHolding<br>Collateral<br>VariationMarginAssetHolding |  |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                    |  |  |

| Collateral | SegregatedIndependentAmountAssetHolding |  |
|------------|-----------------------------------------|--|
| Collateral | CollateralAgreement                     |  |
| Collateral | CollateralOwnership                     |  |
| Collateral | RelatedCollateralSubstitution           |  |
| Collateral | CollateralDeliveryMethod                |  |
| Collateral | CollateralQualityType                   |  |
| Collateral | DeliveryByValue                         |  |
| Collateral | CollateralReinvestment                  |  |
| Collateral | CollateralTransactionType               |  |

| CollateralAgreement |                                | Agreement |
|---------------------|--------------------------------|-----------|
| CollateralAgreement | BaseCurrency                   |           |
| CollateralAgreement | AssociatedMasterAgreement      |           |
| CollateralAgreement | StandingSettlementInstructions |           |
| CollateralAgreement | MarginConvention               |           |
| CollateralAgreement | ExposureTerm                   |           |
| CollateralAgreement | CallFrequency                  |           |
| CollateralAgreement | Collateral                     |           |
| CollateralAgreement | RiskCoverage                   |           |
| CollateralBalance   |                                |           |

| CollateralBalance                | CollateralDescription                             |                    |
|----------------------------------|---------------------------------------------------|--------------------|
| CollateralBalance                | HeldAmount                                        |                    |
| CollateralBalance                | PriorAgreed                                       |                    |
| CollateralBalance                | VariationMarginRelatedRiskCalculation             |                    |
| CollateralBalance                | InTransit                                         |                    |
| CollateralBalance                | SegregatedIndependentAmountRelatedRiskCalculation |                    |
| CollateralBalance                | RelatedCollateralInterestManagement               |                    |
| CollateralBalance                | CollateralInterestManagement                      |                    |
| CollateralInterestAdministration |                                                   | InterestManagement |
| CollateralInterestAdministration | CollateralManagement                              |                    |
| CollateralInterestAdministration | ClosingCollateralBalance                          |                    |
| CollateralInterestAdministration | OpeningCollateralBalance                          |                    |
|                                  |                                                   |                    |

| CollateralManagement |                        |  |
|----------------------|------------------------|--|
| CollateralManagement | CollateralProposal     |  |
| CollateralManagement | CollateralValuation    |  |
| CollateralManagement | FeesAndCommissions     |  |
| CollateralManagement | InterestManagement     |  |
| CollateralManagement | DisputeManagement      |  |
| CollateralManagement | MarginCall             |  |
| CollateralManagement | CollateralSubstitution |  |
| CollateralManagement | RiskToCover            |  |
|                      |                        |  |

| CollateralManagement | Collateral                   |  |
|----------------------|------------------------------|--|
| CollateralManagement | AgreedTerms                  |  |
| CollateralManagement | ClearingSystem               |  |
| CollateralMovement   |                              |  |
| CollateralMovement   | RelatedCollateralProposal    |  |
| CollateralMovement   | VariationMargin              |  |
| CollateralMovement   | SegregatedIndependentAmount  |  |
| CollateralMovement   | MarginCall                   |  |
| CollateralMovement   | SecuritiesCollateralMovement |  |
| CollateralMovement   | CashCollateralMovement       |  |

| CollateralMovement     | FinancialTransaction       |      |
|------------------------|----------------------------|------|
| CollateralPartyRole    |                            | Role |
| CollateralPartyRole    | Collateral                 |      |
| CollateralProposal     |                            |      |
| CollateralProposal     | ProposedCollateralMovement |      |
| CollateralProposal     | ResponseType               |      |
| CollateralProposal     | Type                       |      |
| CollateralProposal     | RelatedManagementProcess   |      |
| CollateralReinvestment |                            |      |
| CollateralReinvestment | CashReinvestmentRate       |      |
|                        |                            |      |

| CollateralReinvestment | ReinvestedCashType                     |        |
|------------------------|----------------------------------------|--------|
| CollateralReinvestment | FundingSourceType                      |        |
| CollateralReinvestment | RelatedCollateral                      |        |
| CollateralStatus       |                                        | Status |
| CollateralStatus       | ResponseStatus                         |        |
| CollateralStatus       | CollateralManagementCancellationReason |        |
| CollateralStatus       | SubstitutionStatus                     |        |
| CollateralStatus       | InterestRejectionReason                |        |
| CollateralStatus       | MarginCallResponse                     |        |
| CollateralStatus       | Settlement                             |        |
| CollateralStatus       | CancellationReason                     |        |
|                        |                                        |        |

| CollateralStatus       | Collateral               |  |
|------------------------|--------------------------|--|
| CollateralSubstitution |                          |  |
| CollateralSubstitution | Type                     |  |
| CollateralSubstitution | AcceptedAmount           |  |
| CollateralSubstitution | RejectedAmount           |  |
| CollateralSubstitution | RelatedManagementProcess |  |
| CollateralSubstitution | NewCollateral            |  |
| CollateralValuation    |                          |  |
| CollateralValuation    | Collateral               |  |
| CollateralValuation    | CollateralValuationDate  |  |
| CollateralValuation    | RelatedManagementProcess |  |
|                        |                          |  |

| CollateralValuation<br>ReportedCurrencyAndAmount<br>CollateralValuation<br>MarketValueAmount<br>CollateralValuation<br>AdjustedRate<br>CollateralValuation<br>CollateralValuationCurrency<br>CollectionAgent<br>SecuritiesPartyRole<br>CommercialTrade<br>Trade<br>CommercialTrade<br>PurchaseAccount<br>CommercialTrade<br>PaymentObligation<br>CommercialTrade<br>TotalAcceptedAmount<br>CommercialTrade<br>PartyRole |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
| CommercialTrade<br>TradeSettlement                                                                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |

| CommercialTrade           | ProductDeliveryObligation |                |
|---------------------------|---------------------------|----------------|
| CommercialTrade           | PurchaseOrder             |                |
| CommercialTrade           | Documents                 |                |
| CommercialTrade           | RelatedUndertaking        |                |
| CommercialTrade           | TransactionStatus         |                |
| CommercialTrade           | Agreement                 |                |
| CommercialTradePartyRole  |                           | TradePartyRole |
| CommercialTradePartyRole  | CommercialTrade           |                |
| CommercialTradeSettlement |                           | Settlement     |
| CommercialTradeSettlement | Payment                   |                |
| CommercialTradeSettlement | Invoice                   |                |
|                           |                           |                |

| CommercialTradeSettlement | LetterOfCredit               |            |
|---------------------------|------------------------------|------------|
| CommercialTradeSettlement | ProductDelivery              |            |
| CommercialTradeSettlement | CommercialTrade              |            |
| Commission                |                              | Adjustment |
| Commission                | CommissionWaiving            |            |
| Commission                | Trade                        |            |
| Commission                | CommissionType               |            |
| Commission                | Basis                        |            |
| Commission                | CommercialAgreementReference |            |
| Commission                | CalculationDate              |            |
| Commission                | Rate                         |            |
| Commission                | CommissionAmount             |            |
|                           |                              |            |

| Commission<br>Broker<br>Commission<br>CommissionPartyRole<br>Commission<br>Account<br>Commission<br>RelatedQuote<br>Commission<br>SplitRate<br>Commission<br>Currency<br>Commission<br>CorporateActionFeesAndCharges<br>CommissionPartyRole<br>Role<br>CommissionPartyRole<br>Commission<br>CommissionRecipient<br>CommissionPartyRole<br>CommissionWaiver<br>CommissionWaiver<br>Commission |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                              |  |  |

| CommissionWaiver  | InstructionBasis   |       |
|-------------------|--------------------|-------|
| CommissionWaiver  | WaivedRate         |       |
| CommissionWaiver  | NonWaivedRate      |       |
| Commodity         |                    | Asset |
| Commodity         | BaseProduct        |       |
| Commodity         | DetailedSubProduct |       |
| Commodity         | SubProduct         |       |
| ComponentSecurity |                    |       |

| ComponentSecurity | SeparationPeriod    |                    |
|-------------------|---------------------|--------------------|
| ComponentSecurity | Security            |                    |
| ComponentSecurity | SeparationChoice    |                    |
| ComponentSecurity | QuantityNumerator   |                    |
| ComponentSecurity | QuantityDenominator |                    |
| ComponentSecurity | SeparationDate      |                    |
| Consignee         |                     | TransportPartyRole |
| Consignor         |                     | TransportPartyRole |
| ContactPersonRole |                     | Role               |
| ContactPersonRole | Role                |                    |
| ContactPersonRole | Meeting             |                    |
|                   |                     |                    |

| ContactPersonRole | Person                      |  |
|-------------------|-----------------------------|--|
| ContactPoint      |                             |  |
| ContactPoint      | Identification              |  |
| ContactPoint      | RelatedInvestmentFund       |  |
| ContactPoint      | BICAddress                  |  |
| ContactPoint      | RelatedParty                |  |
| ContactPoint      | RelatedCorporateActionEvent |  |
| ContactPoint      | RelatedReportingService     |  |
| ContactPoint      | StoredDocument              |  |
| ContactPoint      | RemittanceRelatedPayment    |  |
| ContactPoint      | RelatedProxyAppointment     |  |
| ContactPoint      | ContactPointForMeeting      |  |
| ContactPoint      | ContactPointForVote         |  |

| ContactPoint       | MainContact                   |                          |
|--------------------|-------------------------------|--------------------------|
| ContactPoint       | ReturnAddress                 |                          |
|                    |                               |                          |
| ContactPoint       | RelatedPayment                |                          |
| ContactPoint       | TemporaryIndicator            |                          |
| ContactPoint       | DeliveredAttendanceCard       |                          |
| ContactPoint       | InvestmentFundClassProcessing |                          |
| ContraClearingFirm |                               | SettlementPartyRole      |
| ContraFirm         |                               | SecuritiesTradePartyRole |
| Contract           |                               | Agreement                |
| Contract           | MasterAgreement               |                          |

| CorporateActionAgent<br>CorporateActionPartyRole<br>CorporateActionAgent<br>AgentRole<br>CorporateActionCashEntitlement<br>CorporateActionEntitlement<br>CorporateActionCashEntitlement<br>GrossCashAmount<br>CorporateActionCashEntitlement<br>NetCashAmount<br>CorporateActionCashEntitlement<br>CashInLieuOfShare<br>CorporateActionCashEntitlement<br>CapitalGain<br>CorporateActionCashEntitlement<br>EntitledCashAmount |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |

| CorporateActionCashEntitlement<br>ExchangeRate<br>CorporateActionDeadline<br>Deadline<br>CorporateActionDeadline<br>RevocabilityPeriod<br>CorporateActionDeadline<br>ProtectDate<br>CorporateActionDeadline<br>TradingSuspendedDate<br>CorporateActionDeadline<br>ThirdPartyDeadline<br>CorporateActionDeadline<br>CertificationDeadline<br>CorporateActionDeadline<br>DeadlineToSplit |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                        |  |  |

| CorporateActionDeadline | SpecialExDate                      |  |
|-------------------------|------------------------------------|--|
| CorporateActionDeadline | DeadlineForTaxBreakdownInstruction |  |
| CorporateActionDeadline | EarlyClosingDate                   |  |
| CorporateActionDeadline | RecordDate                         |  |
| CorporateActionDeadline | CoverExpirationDate                |  |
| CorporateActionDeadline | ElectionToCounterpartyDeadline     |  |
| CorporateActionDeadline | ExpiryDate                         |  |
|                         |                                    |  |

| CorporateActionDeadline | EarlyThirdPartyDeadline       |  |
|-------------------------|-------------------------------|--|
| CorporateActionDeadline | DepositoryCoverExpirationDate |  |
| CorporateActionDeadline | ResponseDeadline              |  |
| CorporateActionDeadline | ConsentExpirationDate         |  |
| CorporateActionDeadline | RegistrationDeadline          |  |
| CorporateActionDeadline | StockLendingDeadline          |  |

| CorporateActionDeadline     | ConsentRecordDate           |  |
|-----------------------------|-----------------------------|--|
| CorporateActionDeadline     | EarlyResponseDeadline       |  |
| CorporateActionDeadline     | GuaranteedParticipationDate |  |
| CorporateActionDistribution |                             |  |
| CorporateActionDistribution | PostingQuantity             |  |
| CorporateActionDistribution | PostingDateTime             |  |

| CorporateActionDistribution | MovementDate           |  |
|-----------------------------|------------------------|--|
| CorporateActionDistribution | PostingAmount          |  |
| CorporateActionDistribution | TaxVoucher             |  |
| CorporateActionDistribution | RelatedServicing       |  |
| CorporateActionDistribution | OrderType              |  |
| CorporateActionDistribution | MovementType           |  |
| CorporateActionDistribution | HighPriorityIndicator  |  |
| CorporateActionDistribution | RequestedExecutionDate |  |
| CorporateActionDistribution | FractionTreatment      |  |
| CorporateActionDistribution | CreditDebitIndicator   |  |
| CorporateActionDistribution | Option                 |  |
| CorporateActionDistribution | NetAmount              |  |

| CorporateActionDistribution | GrossAmount                                |  |
|-----------------------------|--------------------------------------------|--|
| CorporateActionDistribution | FinancialTransaction                       |  |
| CorporateActionDistribution | CorporateActionProceedsDeliveryInstruction |  |
| CorporateActionElection     |                                            |  |
| CorporateActionElection     | ExecutionRequestedDateTime                 |  |
| CorporateActionElection     | Option                                     |  |
| CorporateActionElection     | CashAccount                                |  |
| CorporateActionElection     | ElectionType                               |  |
| CorporateActionElection     | Quantity                                   |  |
| CorporateActionElection     | AmendmentReason                            |  |
|                             |                                            |  |

| CorporateActionElection    | RelatedServicing         |              | Process which groups the<br>activities related to corporate<br>action servicing.                                                                                                                                            |                   | CorporateActionServicing      | CorporateActionElection               |
|----------------------------|--------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------------------|---------------------------------------|
| CorporateActionElection    | ProtectProcess           |              | Provides detailed information on<br>protect and cover protect<br>instructions.                                                                                                                                              |                   | CorporateActionProtectProcess | RelatedCorporateActionElection        |
| CorporateActionEntitlement |                          |              | Rights entitled to the account<br>owner based on the terms of the<br>corporate action event and the<br>balance of underlying securities.                                                                                    |                   |                               |                                       |
| CorporateActionEntitlement | EligibleBalance          |              | Total balance of securities eligible<br>for this corporate action event.<br>The entitlement calculation is<br>based on this balance.                                                                                        | SecuritiesBalance |                               | EligibleBalanceRelatedEntitlement     |
| CorporateActionEntitlement | SecuritiesBalance        | entitlement. | Specifies any type of balance<br>related to a corporate action                                                                                                                                                              | SecuritiesBalance |                               | CorporateActionEntitlement            |
| CorporateActionEntitlement | InstructedBalance        |              | Balance of instructed position.                                                                                                                                                                                             | SecuritiesBalance |                               | InstructedBalanceRelatedEntitlement   |
| CorporateActionEntitlement | UninstructedBalance      |              | Balance of uninstructed position.                                                                                                                                                                                           | SecuritiesBalance |                               | UninstructedBalanceRelatedEntitlement |
| CorporateActionEntitlement | EligibleBalanceIndicator |              | Indicates whether the eligible<br>balance is final except for a<br>voluntary corporate action event<br>where it can represent the<br>current eligible balance when<br>communicated before expiration<br>date of that event. | YesNoIndicator    |                               |                                       |
| CorporateActionEntitlement | RelatedServicing         |              | Process which groups the<br>activities related to corporate<br>action servicing.                                                                                                                                            |                   | CorporateActionServicing      | CorporateActionEntitlement            |

| CorporateActionEntitlement<br>NotEligibleBalance<br>CorporateActionEvent<br>CorporateActionEvent<br>Type<br>CorporateActionEvent<br>MandatoryVoluntaryEventType<br>CorporateActionEvent<br>UnderlyingSecurity<br>CorporateActionEvent<br>CorporateActionPrice<br>CorporateActionEvent<br>ExchangeRate<br>CorporateActionEvent<br>RegistrationDetails<br>CorporateActionEvent<br>BasketOrIndexInformation<br>CorporateActionEvent<br>Deadline |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |

| CorporateActionEvent | AdditionalBusinessProcess |  |
|----------------------|---------------------------|--|
| CorporateActionEvent | TradingDate               |  |
| CorporateActionEvent | CorporateActionCharge     |  |
| CorporateActionEvent | PariPassuDate             |  |
| CorporateActionEvent | InformationConditions     |  |
| CorporateActionEvent | FractionalQuantity        |  |
| CorporateActionEvent | EventProcessingType       |  |
| CorporateActionEvent | CorporateActionStatus     |  |
| CorporateActionEvent | AnnouncementDate          |  |
|                      |                           |  |

| CorporateActionEvent | EffectiveDate                  |  |
|----------------------|--------------------------------|--|
| CorporateActionEvent | FurtherDetailsAnnouncementDate |  |
| CorporateActionEvent | MarginFixingDate               |  |
| CorporateActionEvent | ResultPublicationDate          |  |
| CorporateActionEvent | UnconditionalDate              |  |
| CorporateActionEvent | WhollyUnconditionalDate        |  |
| CorporateActionEvent | LapsedDate                     |  |
| CorporateActionEvent | BookClosurePeriod              |  |
| CorporateActionEvent | SecuritiesQuantity             |  |
|                      |                                |  |

| CorporateActionEvent | RestrictionIndicator     |
|----------------------|--------------------------|
| CorporateActionEvent | EventStage               |
| CorporateActionEvent | DocumentationLocation    |
| CorporateActionEvent | SecuritiesQuantitySought |
| CorporateActionEvent | PartialElectionIndicator |
| CorporateActionEvent | CorporateActionPartyRole |
| CorporateActionEvent | MarketClaim              |

| CorporateActionEvent | BiddingConditions                | Specifies the conditions under<br>which securities can be acquired<br>BiddingConditions<br>as part of a corporate action.                                                                                         |
|----------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CorporateActionEvent | RelatedClassAction               | Specifies the underlying class<br>ClassAction<br>action related to the event.                                                                                                                                     |
| CorporateActionEvent | CorporateActionEventRegistration | Official registration of the event.<br>CorporateActionEventRegistration                                                                                                                                           |
| CorporateActionEvent | SuspensionPeriod                 | Period defining the last date for<br>which an action will be accepted<br>and the date on which the<br>SuspensionPeriod<br>suspension will be released and<br>normal processing will resume.                       |
| CorporateActionEvent | Lottery                          | Organisation of draws for cash<br>prizes on bonds (instead of<br>coupon payments). Every issued<br>Lottery<br>bond (similar to a lottery ticket)<br>has an equal opportunity at<br>winning payments in the draws. |
| CorporateActionEvent | MarginType                       | Specifies the margin type for a<br>RemarketingMarginTypeCode<br>remarketing procedure.                                                                                                                            |
| CorporateActionEvent | RelatedMeeting                   | Provides information on the<br>meeting related to the corporate<br>Meeting<br>event.                                                                                                                              |
| CorporateActionEvent | Services                         | Specifies the different services<br>linked to a corporate action<br>CorporateActionServicing<br>event.                                                                                                            |
| CorporateActionEvent | Issuance                         | Information specified when the<br>corporate event relates to the<br>Issuance<br>issuance of securities.                                                                                                           |
| CorporateActionEvent | SecuritiesModification           | Modification of the reference data<br>of a security or of the<br>SecuritiesModification<br>organisation that issued it.                                                                                           |

| CorporateActionEvent<br>TradingPeriod      |                                      |  |
|--------------------------------------------|--------------------------------------|--|
| CorporateActionEvent<br>TransactionTax     |                                      |  |
| CorporateActionEvent<br>ConsentType        |                                      |  |
| CorporateActionEvent<br>ProceedsDefinition |                                      |  |
| CorporateActionEvent                       | TaxOnNonDistributedProceedsIndicator |  |
| CorporateActionEvent                       | AcceptancePriorityLevel              |  |
| CorporateActionEvent<br>DutchAuctionType   |                                      |  |
| CorporateActionEvent<br>FiscalYearPeriod   |                                      |  |
| CorporateActionEventRegistration           |                                      |  |

| CorporateActionEventRegistration | CorporateActionEventIdentification         |         |
|----------------------------------|--------------------------------------------|---------|
| CorporateActionEventRegistration | OfficialCorporateActionEventIdentification |         |
| CorporateActionEventRegistration | OfficialAnnouncementPublicationDate        |         |
| CorporateActionEventRegistration | CorporateActionEvent                       |         |
| CorporateActionFeesAndCharges    |                                            | Charges |
| CorporateActionFeesAndCharges    | CorporateAction                            |         |
| CorporateActionFeesAndCharges    | SolicitationFee                            |         |
| CorporateActionFeesAndCharges    | EarlySolicitationFeeRate                   |         |
| CorporateActionFeesAndCharges    | Commission                                 |         |
|                                  |                                            |         |

| CorporateActionNotification |                                           |                          |
|-----------------------------|-------------------------------------------|--------------------------|
| CorporateActionNotification | RelatedServicing                          |                          |
| CorporateActionNotification | CorporateActionNotificationIdentification |                          |
| CorporateActionNotification | NotificationType                          |                          |
| CorporateActionNotification | CreationDateTime                          |                          |
| CorporateActionOfferor      |                                           | CorporateActionPartyRole |
| CorporateActionOption       |                                           |                          |
| CorporateActionOption       | OptionNumber                              |                          |
| CorporateActionOption       | OptionType                                |                          |
|                             |                                           |                          |

| CorporateActionOption | FractionDisposition            |  |
|-----------------------|--------------------------------|--|
| CorporateActionOption | CurrencyOption                 |  |
| CorporateActionOption | RelatedChoiceCorporateAction   |  |
| CorporateActionOption | CorporateActionElection        |  |
| CorporateActionOption | OptionFeatures                 |  |
| CorporateActionOption | ActionPeriod                   |  |
| CorporateActionOption | OfferType                      |  |
| CorporateActionOption | ChargesAppliedIndicator        |  |
| CorporateActionOption | WithdrawalAllowedIndicator     |  |
| CorporateActionOption | ChangeAllowedIndicator         |  |
| CorporateActionOption | CorporateActionOptionServicing |  |
|                       |                                |  |

| CorporateActionOption<br>ProceedsDefinition            |
|--------------------------------------------------------|
|                                                        |
| CorporateActionOption<br>Distribution                  |
| CorporateActionOption<br>Default                       |
| CorporateActionOption<br>ProrationBelowMinimumQuantity |
| CorporateActionOptionServicing                         |
| CorporateActionOptionServicing<br>RelatedOption        |
| CorporateActionOptionServicing<br>RelatedServicing     |
| CorporateActionPartyRole<br>Role                       |
| CorporateActionPartyRole<br>CorporateActionEvent       |
| CorporateActionPartyRole<br>Account                    |
| CorporateActionPrice                                   |

| CorporateActionPrice | CorporateActionEvent               |  |
|----------------------|------------------------------------|--|
| CorporateActionPrice | CorporateActionExercisePrice       |  |
| CorporateActionPrice | GenericCashPriceReceivedPerProduct |  |
| CorporateActionPrice | GenericCashPricePaidPerProduct     |  |
| CorporateActionPrice | CashInLieuOfSharePrice             |  |
| CorporateActionPrice | OverSubscriptionDepositPrice       |  |
| CorporateActionPrice | CashValueForTax                    |  |

| CorporateActionPrice                       | PricingCalculation                 |  |
|--------------------------------------------|------------------------------------|--|
| CorporateActionPrice                       | MinimumMultipleCashToInstruct      |  |
| CorporateActionPrice                       | MaximumCashToInstruct              |  |
| CorporateActionPrice                       | MinimumCashToInstruct              |  |
| CorporateActionProceedsDeliveryInstruction |                                    |  |
| CorporateActionProceedsDeliveryInstruction | RelatedDistribution                |  |
| CorporateActionProceedsDeliveryInstruction | SecuritiesProceedsMovement         |  |
| CorporateActionProceedsDeliveryInstruction | CashProceedsMovement               |  |
| CorporateActionProceedsDeliveryInstruction | SettlementAccount                  |  |
| CorporateActionProceedsDeliveryInstruction | CorporateActionStandingInstruction |  |
| CorporateActionProtectProcess              |                                    |  |

| CorporateActionProtectProcess        | ProtectDate                    |                            |
|--------------------------------------|--------------------------------|----------------------------|
| CorporateActionProtectProcess        | TransactionIdentification      |                            |
| CorporateActionProtectProcess        | ProtectSafekeepingAccount      |                            |
| CorporateActionProtectProcess        | ProtectTransactionStatus       |                            |
| CorporateActionProtectProcess        | UncoveredProtectQuantity       |                            |
| CorporateActionProtectProcess        | RelatedCorporateActionElection |                            |
| CorporateActionProtectProcess        | TransactionType                |                            |
| CorporateActionSecuritiesEntitlement |                                | CorporateActionEntitlement |
|                                      |                                |                            |

| CorporateActionSecuritiesEntitlement | EntitledSecuritiesQuantity        |                  |
|--------------------------------------|-----------------------------------|------------------|
| CorporateActionSecuritiesEntitlement | RenounceableEntitlementStatusType |                  |
| CorporateActionServicing             |                                   | FinancialService |
| CorporateActionServicing             | SecuritiesAccount                 |                  |
| CorporateActionServicing             | CorporateActionEventNotification  |                  |
| CorporateActionServicing             | CorporateActionDistribution       |                  |
| CorporateActionServicing             | CorporateActionOptionServicing    |                  |
| CorporateActionServicing             | Event                             |                  |
| CorporateActionServicing             | CorporateActionElection           |                  |
|                                      |                                   |                  |

| CorporateActionServicing | CorporateActionEntitlement                 |        |
|--------------------------|--------------------------------------------|--------|
| CorporateActionStatus    |                                            | Status |
| CorporateActionStatus    | AgentStandingInstructionStatus             |        |
| CorporateActionStatus    | ProcessingStatus                           |        |
| CorporateActionStatus    | EventProcessingStatus                      |        |
| CorporateActionStatus    | CorporateActionStatusReason                |        |
| CorporateActionStatus    | InstructionCancellationStatus              |        |
| CorporateActionStatus    | CorporateActionInstructionProcessingStatus |        |
| CorporateActionStatus    | RateStatus                                 |        |
| CorporateActionStatus    | OptionAvailabilityStatus                   |        |
| CorporateActionStatus    | CorporateActionEvent                       |        |
| CorporateActionStatus    | EventStatus                                |        |
| CorporateActionStatus    | RelatedInstructionProcessedStatus          |        |
|                          |                                            |        |

| CorporateActionStatus       | DeactivationDateAndTime           |              |
|-----------------------------|-----------------------------------|--------------|
| CorporateActionStatus       | EventConfirmationStatus           |              |
| CorporateActionStatus       | EventCompletenessStatus           |              |
| CorporateActionStatusReason |                                   | StatusReason |
| CorporateActionStatusReason | CorporateActionCancellationReason |              |
| CorporateActionStatusReason | CorporateActionStatus             |              |
| CorporateActionStatusReason | AcceptedReason                    |              |
| CorporateActionStatusReason | ReversalReason                    |              |
| CorporateActionStatusReason | MovementFailureReason             |              |
| CorporateActionStatusReason | MovementRejectionReason           |              |
| CorporateActionStatusReason | Forwarded                         |              |
| CorporateActionStatusReason | RejectedReason                    |              |
| CorporateActionStatusReason | ReceivedByIssuerOrOfferor         |              |
|                             |                                   |              |

| CorporateActionStatusReason | Returned            |                            |
|-----------------------------|---------------------|----------------------------|
| CorporateInvestor           |                     | InvestmentAccountPartyRole |
| CorrespondentClearingFirm   |                     | SettlementPartyRole        |
| CounterpartyRisk            |                     |                            |
| CounterpartyRisk            | Party               |                            |
| CounterpartyRisk            | ExposedAmount       |                            |
| CounterpartyRisk            | ExposureCalculation |                            |
| CounterpartyRisk            | SecureMarketValue   |                            |
| CounterpartyRisk            | LiquidResourceValue |                            |
| Country                     |                     |                            |

| Country | DomiciledFunds                         |  |
|---------|----------------------------------------|--|
| Country | Code                                   |  |
| Country | Citizen                                |  |
| Country | Tax                                    |  |
| Country | CountryForSafekeepingPlace             |  |
| Country | CountryForBeneficialOwner              |  |
| Country | ProducedProducts                       |  |
| Country | NationalRegulatoryAuthority            |  |
| Country | RelatedCardPayment                     |  |
| Country | Name                                   |  |
| Country | PostalAddressSpecification             |  |
| Country | CountryRelatedInvestmentFundProcessing |  |

| Country            | Market              |  |
|--------------------|---------------------|--|
| Country            | RelatedPaymentCard  |  |
| Country            | SubDivision         |  |
| CountrySubDivision |                     |  |
| CountrySubDivision | Country             |  |
| CountrySubDivision | Province            |  |
| CountrySubDivision | Region              |  |
| CountrySubDivision | County              |  |
| CountrySubDivision | DistrictSubDivision |  |
| CountrySubDivision | State               |  |
| CountrySubDivision | District            |  |

| CountrySubdivisionIdentification |      |  |
|----------------------------------|------|--|
| CountrySubdivisionIdentification | Code |  |
| CountrySubdivisionIdentification | Name |  |
| CouponAttached                   |      |  |
| CouponAttached                   | Date |  |

| CouponAttached    | Number                         |       |
|-------------------|--------------------------------|-------|
| CouponAttached    | Security                       |       |
| CouponAttached    | CouponClippingDate             |       |
| CouponAttached    | Identification                 |       |
| CreditDefaultSwap |                                | Swaps |
| CreditDefaultSwap | RollDate                       |       |
| CreditDefaultSwap | RollMonth                      |       |
| CreditDefaultSwap | Series                         |       |
| CreditInstrument  |                                |       |
| CreditInstrument  | RelatedPayment                 |       |
| CreditInstrument  | Method                         |       |
| CreditInstrument  | CreditInstrumentIdentification |       |
|                   |                                |       |

| CreditInstrument      | NetAmount            |                   |
|-----------------------|----------------------|-------------------|
| CreditInstrument      | Deadline             |                   |
| CreditNote            |                      | FinancialDocument |
| CreditSideTaxDebtor   |                      | TaxPartyRole      |
| CreditTransfer        |                      | IndividualPayment |
| CreditTransfer        | StandingOrder        |                   |
| CreditTransfer        | RelatedStandingOrder |                   |
| CreditTransferMandate |                      | Mandate           |
| CreditTransferMandate | Reason               |                   |
|                       |                      |                   |

| CreditTransferMandate | FirstPaymentDate     |                  | Date of the first payment of a<br>recurrent credit transfer as per<br>the mandate.                                                                   | ISODateTime             |                           |
|-----------------------|----------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|---------------------------|
| CreditTransferMandate | DateOfVerification   |                  | Date on which the credit transfer<br>mandate has been verified.                                                                                      | ISODateTime             |                           |
| CreditTransferMandate | FinalPaymentDate     |                  | Date of the final payment of a<br>recurrent credit transfer as per<br>the mandate.                                                                   | ISODateTime             |                           |
| CreditTransferMandate | Signature            |                  | Additional security provisions,<br>such as a digital signature, as<br>provided by the debtor.                                                        | Max10KBinary            |                           |
| CreditorAgentRole     |                      | PaymentPartyRole | Financial institution servicing an<br>account for the creditor.                                                                                      |                         |                           |
| CreditorRole          |                      | PaymentPartyRole | Party to which an amount of<br>money is due.                                                                                                         |                         |                           |
| CreditorRole          | SchemeIdentification |                  | Credit party that signs a direct<br>debit mandate.                                                                                                   | Scheme                  | CreditorRole              |
| CrossTrade            |                      | SecuritiesOrder  | Transaction where either the<br>buy-broker and the sell-broker<br>are the same, or the buy-broker<br>and the sell-broker belong to the<br>same firm. |                         |                           |
| CrossTrade            | BuySideOrder         |                  | Buyside order details.                                                                                                                               | SecuritiesOrder         | BuySideRelatedCrossTrade  |
| CrossTrade            | SellSideOrder        |                  | Sell side order details.                                                                                                                             | SecuritiesOrder         | SellSideRelatedCrossTrade |
| CrossTrade            | ExecutionType        |                  | Identifies the type of execution<br>of a cross trade.                                                                                                | CrossTradeExecutionCode |                           |
| CrossTrade            | CrossType            |                  | Type of cross being submitted to<br>a market.                                                                                                        | CrossTypeCode           |                           |

| CrossTrade       | Prioritisation                          |  |
|------------------|-----------------------------------------|--|
| CurrencyExchange |                                         |  |
| CurrencyExchange | OriginalAmount                          |  |
| CurrencyExchange | CurrencyExchangeForForeignExchangeTrade |  |
| CurrencyExchange | UnitCurrency                            |  |
| CurrencyExchange | QuotedCurrency                          |  |
|                  |                                         |  |

| CurrencyExchange | ExchangeRate                         |  |
|------------------|--------------------------------------|--|
| CurrencyExchange | ResultingAmount                      |  |
| CurrencyExchange | RelatedCorporateActionEvent          |  |
| CurrencyExchange | CurrencyExchangeForSecuritiesBalance |  |
| CurrencyExchange | QuotationDate                        |  |
| CurrencyExchange | CalculatedAssetValue                 |  |
| CurrencyExchange | SourceCurrency                       |  |
| CurrencyExchange | TargetCurrency                       |  |
| CurrencyExchange | CurrencyExchangeForCashEntry         |  |
|                  |                                      |  |

| CurrencyExchange | RelatedPayment                                    |  |
|------------------|---------------------------------------------------|--|
| CurrencyExchange | RateType                                          |  |
| CurrencyExchange | RelatedLimitManagement                            |  |
| CurrencyExchange | FixingConditions                                  |  |
| CurrencyExchange | Tax                                               |  |
| CurrencyExchange | RelatedInvoice                                    |  |
| CurrencyExchange | CurrencyExchangeForTransactionAdministrator       |  |
| CurrencyExchange | ReportedAccount                                   |  |
| CurrencyExchange | CurrencyExchangeForCorporateActionCashEntitlement |  |
| CurrencyExchange | PaymentExecution                                  |  |
| CurrencyExchange | CurrencyExchangeForSecuritiesQuote                |  |
|                  |                                                   |  |

| CurrencyExchange | CurrencyExchangeForSecuritiesConversion |               |
|------------------|-----------------------------------------|---------------|
| CurrencyExchange | CurrencyExchangeForCashDistribution     |               |
| CurrencyExchange | Adjustment                              |               |
| CurrencyExchange | RelatedPaymentTracker                   |               |
| CurrencyExchange | ExchangeRateBase                        |               |
| CurrencyExchange | QuoteIdentification                     |               |
| CurrencyExchange | ForeignExchangeAgent                    |               |
| CurrencyOption   |                                         | TreasuryTrade |
| CurrencyOption   | CallAmount                              |               |
|                  |                                         |               |

| CurrencyOption   | PutAmount                |                   |
|------------------|--------------------------|-------------------|
| CurrencyOption   | PremiumCalculation       |                   |
| CurrencyOption   | OptionDefinition         |                   |
| CurrencyOption   | PremiumSettlement        |                   |
| CurrencyOption   | ExercisedOption          |                   |
| CurrencyOption   | OptionSettlementCurrency |                   |
| CurrencyOption   | StrikeRate               |                   |
| CurrencyStrategy |                          | PortfolioStrategy |
| CurrencyStrategy | Currency                 |                   |
| Curve            |                          |                   |
| Curve            | Currency                 |                   |
| Curve            | Name                     |                   |
|                  |                          |                   |

| Curve             | Point          |                            |
|-------------------|----------------|----------------------------|
| Curve             | Spread         |                            |
| CustodianForMinor |                | InvestmentAccountPartyRole |
| CustodianRole     |                | SecuritiesPartyRole        |
| CustodianRole     | InvestmentFund |                            |
| CustodyService    |                | FinancialService           |
| DataSetInitiator  |                | CardPaymentPartyRole       |
| DateTimePeriod    |                |                            |
| DateTimePeriod    | FromDateTime   |                            |

| DateTimePeriod | ToDateTime                         |  |
|----------------|------------------------------------|--|
| DateTimePeriod | RelatedStandingOrder               |  |
| DateTimePeriod | PaymentInstruction                 |  |
| DateTimePeriod | NumberOfDays                       |  |
| DateTimePeriod | ValuationStatistics                |  |
| DateTimePeriod | PerformanceFactors                 |  |
| DateTimePeriod | Status                             |  |
| DateTimePeriod | PriceCalculationRelatedPricing     |  |
| DateTimePeriod | CorporateActionOption              |  |
| DateTimePeriod | ParallelTradingProceedsDefinition  |  |
| DateTimePeriod | PrivilegeSuspensionCorporateAction |  |
| DateTimePeriod | WithdrawalSuspensionRelatedEvent   |  |
|                |                                    |  |

| DateTimePeriod | RelatedInterestCalculation                    |  |
|----------------|-----------------------------------------------|--|
| DateTimePeriod | BiddingConditions                             |  |
| DateTimePeriod | ClassAction                                   |  |
| DateTimePeriod | BookEntryTransferSuspensionRelatedEvent       |  |
| DateTimePeriod | DepositAtAgentSuspensionRelatedEvent          |  |
| DateTimePeriod | DepositSuspensionRelatedEvent                 |  |
| DateTimePeriod | PledgeSuspensionRelatedEvent                  |  |
| DateTimePeriod | SegregationPeriodRelatedEvent                 |  |
| DateTimePeriod | WithdrawalAtAgentSuspensionRelatedEvent       |  |
| DateTimePeriod | WithdrawalInNomineeNameSuspensionRelatedEvent |  |
|                |                                               |  |

| DateTimePeriod | WithdrawalInStreetNameSuspensionRelatedEvent |  |
|----------------|----------------------------------------------|--|
| DateTimePeriod | BookClosureCorporateAction                   |  |
| DateTimePeriod | CoDepositoriesSuspensionRelatedEvent         |  |
| DateTimePeriod | ExtendiblePeriodDebt                         |  |
| DateTimePeriod | SecuritiesConversion                         |  |
| DateTimePeriod | YieldCalculation                             |  |
| DateTimePeriod | CustomDateDebt                               |  |
| DateTimePeriod | TaxPeriod                                    |  |
| DateTimePeriod | Account                                      |  |
| DateTimePeriod | RelatedAgreement                             |  |
| DateTimePeriod | AssentedLinePeriodProceedsDefinition         |  |

| DateTimePeriod<br>SellThruIssuerProceedsDefinition |
|----------------------------------------------------|
| DateTimePeriod<br>RelatedProductDelivery           |
| DateTimePeriod<br>RelatedInvoice                   |
| DateTimePeriod<br>TradeCertificate                 |
| DateTimePeriod<br>RelatedPortfolioValuation        |
| DateTimePeriod<br>System                           |
| DateTimePeriod<br>AccountRestriction               |
| DateTimePeriod<br>BankOperation                    |
| DateTimePeriod<br>RelatedCorporateAction           |
| DateTimePeriod<br>RelatedLimit                     |
| DateTimePeriod<br>RelatedIdentification            |
| DateTimePeriod<br>AssessmentValidityScheme         |

| DateTimePeriod | ExercisePeriodDistribution |  |
|----------------|----------------------------|--|
| DateTimePeriod | OfferPeriodDistribution    |  |
| DateTimePeriod | TradingPeriodDistribution  |  |
| DateTimePeriod | BlockingPeriodDistribution |  |
| DateTimePeriod | Guarantee                  |  |
| DateTimePeriod | PriceFactRelatedPricing    |  |
| DateTimePeriod | CashDistribution           |  |
| DateTimePeriod | ComponentSecurity          |  |
| DateTimePeriod | TradingSession             |  |
| DateTimePeriod | FinancialInstrumentSwap    |  |
| DateTimePeriod | RelatedPostalAddress       |  |
| DateTimePeriod | RedemptionSchedule         |  |
|                |                            |  |

| DateTimePeriod | RelatedAccountLink                   | Link between two accounts for<br>which a validity period is<br>AccountLink<br>specified.                                |  |
|----------------|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--|
| DateTimePeriod | RelatedAdjustment                    | Adjustment for which a validity<br>Adjustment<br>period is provided.                                                    |  |
| DateTimePeriod | RelatedSecuritiesIdentification      | Securities identification for which<br>SecuritiesIdentification<br>a validity period is specified.                      |  |
| DateTimePeriod | RelatedStandingSettlementInstruction | SSI for which a validity period is<br>StandingSettlementInstruction<br>specified.                                       |  |
| DateTimePeriod | RelatedSecuritiesRegistration        | Securities registration process for<br>BasicSecuritiesRegistration<br>which a split period is specified.                |  |
| DateTimePeriod | Amount                               | Relationship with an amount.<br>AmountAndPeriod                                                                         |  |
| DateTimePeriod | RelatedInvestmentPlan                | InvestmentPlan for which an<br>InvestmentPlan<br>investment period is specified.                                        |  |
| DateTimePeriod | Issuance                             | Issuance for which subscription<br>Issuance<br>information is provided.                                                 |  |
| DateTimePeriod | RelatedPaymentTerms                  | Payment terms for which a<br>PaymentTerms<br>period is specified.                                                       |  |
| DateTimePeriod | Percentage                           | Relationship with a percentage.<br>PercentageAndPeriod                                                                  |  |
| DateTimePeriod | RelatedRolePlayer                    | Role player for which a validity<br>RolePlayer<br>period is specified.                                                  |  |
| DateTimePeriod | RelatedSystemAvailability            | System availability for which the<br>SystemAvailability<br>closure period is provided.                                  |  |
| Deadline       |                                      | Specifies the different deadlines<br>available for the different<br>processes related to corporate<br>action processes. |  |

| Deadline           | RelatedCorporateActionEvent |
|--------------------|-----------------------------|
| Deadline           | MarketDeadline              |
| Deadline           | IntermediaryDeadline        |
| Deadline           | STPDeadline                 |
| Deadline           | RelatedMeeting              |
| DebitAuthorisation |                             |
| DebitAuthorisation | ValueDateToDebit            |
| DebitAuthorisation | DebitAuthorisationDecision  |
| DebitAuthorisation | AmountToDebit               |

| DebitAuthorisation  | Reason                             |                    |
|---------------------|------------------------------------|--------------------|
| DebitAuthorisation  | AuthorisedReturn                   |                    |
| DebitAuthorisation  | RelatedInvestigationCaseResolution |                    |
| DebitCreditFacility |                                    | CashAccountService |
| DebitCreditFacility | CreditLine                         |                    |
| DebitCreditFacility | CashAccountInterest                |                    |
| DebitCreditFacility | CreditDebitIndicator               |                    |
| DebitSideTaxDebtor  |                                    | TaxPartyRole       |
| Debt                |                                    | Security           |

| Debt | PaymentDirectionIndicator |  |
|------|---------------------------|--|
| Debt | NextCallableDate          |  |
| Debt | PutableDate               |  |
| Debt | DatedDate                 |  |
| Debt | FirstPaymentDate          |  |

| Debt | Factor                |  |
|------|-----------------------|--|
| Debt | PoolNumber            |  |
| Debt | VariableRateIndicator |  |
| Debt | CallableIndicator     |  |
| Debt | PutableIndicator      |  |
| Debt | YieldToMaturityRate   |  |

| Debt | AccruedCapitalisationAmount |  |
|------|-----------------------------|--|
| Debt | NextCouponDate              |  |
| Debt | NextFactorDate              |  |
| Debt | OddCouponIndicator          |  |
| Debt | CPProgram                   |  |
| Debt | CPRegistrationType          |  |
| Debt | ConvertibleIndicator        |  |
| Debt | PreFundedIndicator          |  |

| Debt | EscrowedIndicator     |  |
|------|-----------------------|--|
| Debt | PerpetualIndicator    |  |
| Debt | SubordinatedIndicator |  |
| Debt | ExtendibleIndicator   |  |
| Debt | ExtendiblePeriod      |  |
| Debt | OverAllotmentAmount   |  |
| Debt | OverAllotmentRate     |  |
| Debt | AmortisableIndicator  |  |
|      |                       |  |

| Debt | CapitalisedInterest       |  |
|------|---------------------------|--|
| Debt | ActualDenominationAmount  |  |
| Debt | Pieces                    |  |
| Debt | PoolsMaximum              |  |
| Debt | PoolsPerMillion           |  |
| Debt | PoolsPerLot               |  |
| Debt | PoolsPerTrade             |  |
| Debt | ConstantPrePaymentPenalty |  |
|      |                           |  |

| Debt | PrePaymentSpeed         |  |
|------|-------------------------|--|
| Debt | ConstantPrePaymentYield |  |
| Debt | WeightedAverageCoupon   |  |
| Debt | WeightedAverageLife     |  |
| Debt | WeightedAverageLoan     |  |
| Debt | WeightedAverageMaturity |  |
| Debt | InsuredIndicator        |  |
| Debt | BankQualified           |  |

| Debt<br>AutoReinvestment<br>Debt<br>CustomDate<br>Debt<br>LookBack<br>Debt<br>MinimumDenomination<br>Debt<br>MaximumSubstitution<br>Debt<br>MinimumIncrement<br>Debt<br>Production<br>Debt<br>Restricted |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |

| Debt<br>PriceFrequency<br>Debt<br>SubstitutionFrequency<br>Debt<br>SubstitutionLeft<br>Debt<br>WholePool<br>Debt<br>AlternativeMinimumTax<br>Debt<br>NextInterest<br>Debt<br>ExtendibleDate<br>Debt<br>SinkableIndicator |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |

| Debt            | Insured         |                  |
|-----------------|-----------------|------------------|
| Debt            | Geographics     |                  |
| Debt            | PaymentCurrency |                  |
| Debt            | DirtyPrice      |                  |
| Debt            | DebtSeniority   |                  |
| DebtorAgentRole |                 | PaymentPartyRole |
| DebtorRole      |                 | PaymentPartyRole |

| DefaultFund             |                       |  |
|-------------------------|-----------------------|--|
| DefaultFund             | TotalAmount           |  |
| DefaultFund             | Contribution          |  |
| DefaultFund             | ClearingSystem        |  |
| DefaultFundContribution |                       |  |
| DefaultFundContribution | RelatedMarginCall     |  |
| DefaultFundContribution | DefaultFund           |  |
| DefaultFundContribution | ExcessOrDeficitAmount |  |
|                         |                       |  |

| DefaultFundContribution | ContributionAccount |                               |
|-------------------------|---------------------|-------------------------------|
| DefaultFundContribution | AmountDirection     |                               |
| DeliverersCustodian     |                     | SecuritiesSettlementPartyRole |
| DeliverersIntermediary  |                     | SecuritiesSettlementPartyRole |
| DeliveringAgent         |                     | SecuritiesSettlementPartyRole |

| DeliveringDepositoryRole  |                           | DeliveringSettlementParty     |
|---------------------------|---------------------------|-------------------------------|
| DeliveringSettlementParty |                           | SecuritiesSettlementPartyRole |
| DeliveringSettlementParty | DeliveringSettlementParty |                               |
| DeliveringSettlementParty | NextParty                 |                               |
| DeliveryNote              |                           | Document                      |
| Demand                    |                           |                               |

| Demand  | Undertaking        |       |
|---------|--------------------|-------|
| Demand  | SubmissionDateTime |       |
| Demand  | DemandAmount       |       |
| Demand  | Type               |       |
| Demand  | TotalClaimAmount   |       |
| Demand  | Payment            |       |
| Demand  | AssociatedDocument |       |
| Deposit |                    | Money |
| Deposit | DepositType        |       |
| Deposit | Interest           |       |

| DepositoryRole |                           | SecuritiesPartyRole |
|----------------|---------------------------|---------------------|
| Derivative     |                           | Asset               |
| Derivative     | UnderlyingAsset           |                     |
| Derivative     | NotionalCurrencyAndAmount |                     |
| Derivative     | DerivativeCovered         |                     |
| Derivative     | ExerciseDate              |                     |
| Derivative     | InterestIncludedInPrice   |                     |
| Derivative     | Tick                      |                     |
| Derivative     | ExercisePrice             |                     |

| Derivative         | NotionalCurrency       |                     |
|--------------------|------------------------|---------------------|
| Derivative         | VersionNumber          |                     |
| Derivative         | Event                  |                     |
| DerivativeEvent    |                        |                     |
| DerivativeEvent    | EventIdentifier        |                     |
| DerivativeEvent    | RelatedDerivative      |                     |
| DerivativeEvent    | TimeStamp              |                     |
| DerivativeEvent    | PostTradeRiskReduction |                     |
| DerivativeEvent    | Type                   |                     |
| DeterminationAgent |                        | SecuritiesPartyRole |
|                    |                        |                     |

| DigitalWallet |                            | SecuritiesAccount |
|---------------|----------------------------|-------------------|
| DigitalWallet | DigitalAssetIdentifier     |                   |
| DirectDebit   |                            | IndividualPayment |
| DirectDebit   | RegistrationIdentification |                   |
| DirectDebit   | DirectDebitMandate         |                   |

| DirectDebit        | PreNotificationIdentification |         |
|--------------------|-------------------------------|---------|
| DirectDebit        | PreNotificationDate           |         |
| DirectDebitMandate |                               | Mandate |
| DirectDebitMandate | RelatedDirectDebit            |         |
| DirectDebitMandate | FinalCollectionDate           |         |
| DirectDebitMandate | FirstCollectionDate           |         |
| DirectDebitMandate | CollectionAmount              |         |
| DirectDebitMandate | MaximumAmount                 |         |
|                    |                               |         |

| DirectDebitMandate   | PreNotification             |                  |
|----------------------|-----------------------------|------------------|
| DirectDebitMandate   | PreNotificationThreshold    |                  |
| DirectDebitMandate   | Classification              |                  |
| DirectDebitMandate   | PointInTime                 |                  |
| DirectMember         |                             | SystemMemberRole |
| DisclosedListTrading |                             | ListTrading      |
| DisclosedListTrading | DisclosedListTradingAccount |                  |
| DisclosedListTrading | BuyAmount                   |                  |

| DisclosedListTrading | SellAmount                  |            |
|----------------------|-----------------------------|------------|
| DisclosedListTrading | RequestedSettlementDateCode |            |
| Discount             |                             | Adjustment |
| Discount             | DiscountAppliedAmount       |            |
| Discount             | DiscountType                |            |
| Discount             | DiscountBasisAmount         |            |
| Discrepancy          |                             |            |
| Discrepancy          | UndertakingStatusReason     |            |
| Discrepancy          | Type                        |            |
| Discrepancy          | Description                 |            |
| Discretion           |                             |            |
|                      |                             |            |

| Discretion        | RelatedOrderExecution |  |
|-------------------|-----------------------|--|
| Discretion        | Offset                |  |
| Discretion        | OffsetSign            |  |
| Discretion        | RelatedPriceType      |  |
| Discretion        | MoveType              |  |
| Discretion        | LimitType             |  |
| Discretion        | RoundDirection        |  |
| Discretion        | Scope                 |  |
| Discretion        | OffsetType            |  |
| DisputeManagement |                       |  |
| DisputeManagement | DisputedAmount        |  |

| DisputeManagement | DisputeDate              |  |
|-------------------|--------------------------|--|
| DisputeManagement | DisputeResolutionType    |  |
| DisputeManagement | RelatedManagementProcess |  |
| Distribution      |                          |  |
| Distribution      | ExercisePeriod           |  |
| Distribution      | OfferPeriod              |  |
| Distribution      | TradingPeriod            |  |
| Distribution      | BlockingPeriod           |  |
| Distribution      | InterestPeriod           |  |
| Distribution      | DistributionTax          |  |
| Distribution      | OfferPrice               |  |

| Distribution | IncentivePremium |  |
|--------------|------------------|--|
| Distribution | EffectiveDate    |  |
| Distribution | EventConditions  |  |
| Distribution | ExDate           |  |
| Distribution | GrossRate        |  |
| Distribution | MeetingDate      |  |
| Distribution | NetRate          |  |
| Distribution | NewFaceValue     |  |
| Distribution | NewParValue      |  |
| Distribution | PaymentDate      |  |
|              |                  |  |

| Distribution | Dividend                |  |
|--------------|-------------------------|--|
| Distribution | CorporateActionOption   |  |
| Distribution | CurrencyOption          |  |
| Distribution | DecreaseAmount          |  |
| Distribution | DecreaseRate            |  |
| Distribution | OfferPriceFixingDate    |  |
| Dividend     |                         |  |
| Dividend     | DividendFrequency       |  |
| Dividend     | AnnualTotalDividendRate |  |
| Dividend     | FinalDividend           |  |

| Dividend | FullyFrankedRateAndAmount  |  |
|----------|----------------------------|--|
| Dividend | GrossDividend              |  |
| Dividend | RateType                   |  |
| Dividend | NetDividend                |  |
| Dividend | ProvisionalDividend        |  |
| Dividend | DividendRankingDate        |  |
| Dividend | ManufacturedDividendAmount |  |
| Dividend | UnfrankedAmount            |  |

| Dividend | NotionalDividendPayableAmount | Amount of cash that would have<br>been payable if the dividend had<br>CurrencyAndAmount<br>been taken in the form of cash<br>rather than shares.    |
|----------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Dividend | Rate                          | Planned dividend rate, for<br>PercentageRate<br>example, for preferred shares.                                                                      |
| Dividend | ExDividendDate                | Date/time as from which trading<br>(including exchange and OTC<br>ISODateTime<br>trading) occurs on the underlying<br>security without the benefit. |
| Dividend | Security                      | Security for which a dividend is<br>Security<br>specified.                                                                                          |
| Dividend | Type                          | Nature of the dividend.<br>DividendTypeCode                                                                                                         |
| Dividend | CashProceeds                  | Defines the proceeds which<br>CashProceedsDefinition<br>resulted in dividends.                                                                      |
| Dividend | Obligation                    | Specifies the payment terms of<br>PaymentObligation<br>the dividend.                                                                                |
| Dividend | Tax                           | Tax on dividend.<br>Tax                                                                                                                             |
| Dividend | RelatedDistribution           | Distribution for which a dividend<br>Distribution<br>is specified.                                                                                  |
| Dividend | DividendFrequenceType         | Specifies the cycle of dividends.<br>CorporateActionFrequencyTypeCode                                                                               |
| Dividend | DividendRatio                 | Percentage of earnings paid to<br>PercentageRate<br>shareholders in dividends.                                                                      |
| Dividend | PaymentDate                   | Date upon which the dividend is<br>ISODate<br>paid.                                                                                                 |
| Dividend | PaymentFrequency              | Specifies the cycle of dividend<br>FrequencyCode<br>payments.                                                                                       |

| Dividend | ReinvestmentDate           |  |
|----------|----------------------------|--|
| Dividend | Value                      |  |
| Dividend | DeemedAmount               |  |
| Dividend | DeemedRate                 |  |
| Dividend | ConduitForeignIncomeAmount |  |
| Document |                            |  |
| Document | IssueDate                  |  |
| Document | CopyDuplicate              |  |
| Document | PlaceOfStorage             |  |
| Document | PaymentObligation          |  |
| Document | Type                       |  |

| Document | Amount          |  |
|----------|-----------------|--|
| Document | Agreement       |  |
| Document | PlaceOfIssue    |  |
| Document | DocumentVersion |  |
| Document | Status          |  |
| Document | Reconciliation  |  |
| Document | LetterOfCredit  |  |
| Document | PartyRole       |  |
| Document | DataSetType     |  |
| Document | Transport       |  |
| Document | SignedIndicator |  |

| Document          | RemittedAmount         |                   |
|-------------------|------------------------|-------------------|
| Document          | Guarantee              |                   |
| Document          | Language               |                   |
| Document          | Purpose                |                   |
| Document          | DocumentIdentification |                   |
| Document          | Evidence               |                   |
| Document          | CommercialTrade        |                   |
| Document          | Presentation           |                   |
| Document          | RelatedContract        |                   |
| DocumentIssuer    |                        | DocumentPartyRole |
| DocumentPartyRole |                        | Role              |

| DocumentPartyRole | Document                       |                   |
|-------------------|--------------------------------|-------------------|
| DocumentSignatory |                                | DocumentPartyRole |
| Drawdown          |                                |                   |
| Drawdown          | BeneficiaryType                |                   |
| Drawdown          | CrystallisedUnitsNumber        |                   |
| Drawdown          | CrystallisationAmount          |                   |
| Drawdown          | DrawdownStatus                 |                   |
| Drawdown          | EventType                      |                   |
| Drawdown          | TrancheType                    |                   |
| Drawdown          | PercentageOfTotalTransferValue |                   |
| Drawdown          | ApplicableRules                |                   |
| Drawdown          | CappedLimit                    |                   |
| Drawdown          | Beneficiary                    |                   |

| Drawdown      | TriggeredDate                 |                         |
|---------------|-------------------------------|-------------------------|
| Drawdown      | EventDate                     |                         |
| Drawdown      | DrawdownAmount                |                         |
| Drawdown      | Pension                       |                         |
| Drawdown      | LifetimeAllowance             |                         |
| Drawdown      | DrawdownTrancheIdentification |                         |
| Drawdown      | NumberOfDrawdownTranches      |                         |
| Drawee        |                               | ChequePartyRole         |
| Drawer        |                               | ChequePartyRole         |
| DuplicateCase |                               | InvestigationResolution |
| DuplicateCase | DuplicatedCase                |                         |
| DuplicateCase | RelatedCaseResolution         |                         |
|               |                               |                         |

| DurationCalculation |                          |                          |
|---------------------|--------------------------|--------------------------|
| DurationCalculation | RelatedSecuritiesPricing |                          |
| DurationCalculation | VariableInterest         |                          |
| DurationCalculation | Years                    |                          |
| DurationCalculation | CalculationType          |                          |
| DurationCalculation | ValueDate                |                          |
| DurationCalculation | ValuePeriod              |                          |
| ETCServiceProvider  |                          | SecuritiesTradePartyRole |
| ElectronicAddress   |                          | ContactPoint             |
| ElectronicAddress   | EmailAddress             |                          |
| ElectronicAddress   | URLAddress               |                          |

| ElectronicAddress                  | TelexAddress                            |                |
|------------------------------------|-----------------------------------------|----------------|
| ElectronicAddress                  | RelatedPresentation                     |                |
| ElectronicAddress                  | TeletextAddress                         |                |
| ElectronicAddress                  | ISDNAddress                             |                |
| ElectronicInvoiceProcessingService |                                         | AccountService |
| ElectronicInvoiceProcessingService | RelatedInvoice                          |                |
| ElectronicInvoiceProcessingService | ElectronicInvoiceSolutionProvider       |                |
| ElectronicInvoiceProcessingService | CreditorEnrolment                       |                |
| ElectronicInvoiceProcessingService | ElectronicInvoiceDirectoryProvider      |                |
| ElectronicInvoiceProcessingService | DebtorActivation                        |                |
| ElectronicInvoiceProcessingService | ProcessingStatus                        |                |
| ElectronicInvoiceServiceProvider   |                                         | Role           |
| ElectronicInvoiceServiceProvider   | RelatedElectronicInvoiceSolutionService |                |

| ElectronicInvoiceServiceProvider | ServiceStatus                             |           |
|----------------------------------|-------------------------------------------|-----------|
| ElectronicInvoiceServiceProvider | RelatedElectronicInvoiceDirectoryService  |           |
| ElectronicInvoiceServiceStatus   |                                           |           |
| ElectronicInvoiceServiceStatus   | ServiceStatus                             |           |
| ElectronicInvoiceServiceStatus   | ActivationStatusReason                    |           |
| ElectronicInvoiceServiceStatus   | EnrolmentStatusReason                     |           |
| ElectronicInvoiceServiceStatus   | StatusReasonOriginator                    |           |
| ElectronicInvoiceServiceStatus   | RelatedElectronicinvoiceProcessingService |           |
| ElectronicSignature              |                                           | Signature |
| ElectronicSignature              | Undertaking                               |           |
| ElectronicSignature              | RelatedSecurityCertificate                |           |
| EmployingPartyRole               |                                           | Role      |
|                                  |                                           |           |

| EmployingPartyRole | Employee             |           |
|--------------------|----------------------|-----------|
| Energy             |                      | Commodity |
| Energy             | WeekDay              |           |
| Energy             | LoadType             |           |
| Energy             | Delivery             |           |
| Energy             | Duration             |           |
| Energy             | Price                |           |
| Energy             | QuantityUnit         |           |
| Energy             | InterConnectionPoint |           |
| Energy             | Date                 |           |
| EnergyDelivery     |                      |           |
| EnergyDelivery     | PointOrZone          |           |
| EnergyDelivery     | Capacity             |           |
| EnergyDelivery     | Interval             |           |
| EnergyDelivery     | RelatedEnergy        |           |
| EnrolmentService   |                      |           |
|                    |                      |           |

| EnrolmentService | ServiceActivationLink                     |  |
|------------------|-------------------------------------------|--|
| EnrolmentService | ServiceActivationAllowed                  |  |
| EnrolmentService | EndDate                                   |  |
| EnrolmentService | UltimateCreditor                          |  |
| EnrolmentService | Visibility                                |  |
| EnrolmentService | ServiceDescriptionLink                    |  |
| EnrolmentService | StartDate                                 |  |
| EnrolmentService | Creditor                                  |  |
| EnrolmentService | OriginalEnrolment                         |  |
| EnrolmentService | RelatedElectronicInvoiceProcessingService |  |

| EnrolmentService<br>RelatedEnrolment<br>EnrolmentVisibility<br>EnrolmentVisibility<br>EndDate<br>EnrolmentVisibility<br>RelatedEnrolmentService<br>EnrolmentVisibility<br>LimitedVisibility<br>EnrolmentVisibility<br>StartDate<br>EnteringFirm<br>SecuritiesOrderPartyRole<br>Entitlement<br>Security<br>Entitlement<br>StrikePrice |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |

| Entitlement | CoveredIndicator     |  |
|-------------|----------------------|--|
| Entitlement | OptionStyle          |  |
| Entitlement | OptionType           |  |
| Entitlement | CappedValue          |  |
| Entitlement | CappedIndicator      |  |
| Entry       |                      |  |
| Entry       | CreditDebitIndicator |  |
| Entry       | EntryDate            |  |
| Entry       | Identification       |  |
|             |                      |  |

| Entry | AccountOwnerTransactionIdentification    |  |
|-------|------------------------------------------|--|
| Entry | AccountServicerTransactionIdentification |  |
| Entry | ReversalIndicator                        |  |
| Entry | ValueDate                                |  |
| Entry | BankTransactionCode                      |  |
| Entry | CommissionWaiverIndicator                |  |
| Entry | Role                                     |  |
| Entry | Account                                  |  |
| Entry | Balance                                  |  |
| Entry | EntryType                                |  |
|       |                                          |  |

| Equalisation |                                  |  |
|--------------|----------------------------------|--|
| Equalisation | Amount                           |  |
| Equalisation | Date                             |  |
| Equalisation | Rate                             |  |
| Equalisation | RelatedInvestmentFundTransaction |  |
| Equalisation | CreditDebitIndicator             |  |
| Equalisation | DepreciationDepositPerUnit       |  |

| Equalisation | CreditPerUnit   |  |
|--------------|-----------------|--|
| Equalisation | MethodologyType |  |
| Equalisation | HighWatermark   |  |
| Equalisation | GrossAssetValue |  |

| Equalisation | ContingentLiquidationPerUnit |          |
|--------------|------------------------------|----------|
| Equity       |                              | Security |
| Equity       | PreferenceToIncome           |          |
| Equity       | ConvertibleIndicator         |          |

| Equity                   | NonPaidAmount        |  |
|--------------------------|----------------------|--|
| Equity                   | ParValue             |  |
| Equity                   | VotingRightsPerShare |  |
| Evidence                 |                      |  |
| Evidence                 | RelatedDocument      |  |
| ExchangeForPhysicalTrade |                      |  |
| ExchangeForPhysicalTrade | OutsideIndex         |  |
| ExchangeForPhysicalTrade | FairValue            |  |
| ExchangeForPhysicalTrade | ValueForFutures      |  |
| ExchangeForPhysicalTrade | OutMainCountryIndex  |  |
|                          |                      |  |

| ExchangeForPhysicalTrade | SecuritiesOrder            |                          |
|--------------------------|----------------------------|--------------------------|
| ExecutingBrokerRole      |                            | Broker                   |
| ExecutingBrokerRole      | ExecutingTrader            |                          |
| ExecutingPerson          |                            | SecuritiesOrderPartyRole |
| ExecutingTrader          |                            | SecuritiesTradePartyRole |
| ExecutingTrader          | ExecutingBroker            |                          |
| ExecutionDestination     |                            | SecuritiesTradePartyRole |
| ExpectedCollateralType   |                            |                          |
| ExpectedCollateralType   | VariationMarginRelatedCall |                          |
| ExpectedCollateralType   | Delivery                   |                          |
| ExpectedCollateralType   | Return                     |                          |
|                          |                            |                          |

| ExpectedCollateralType | SegregatedIndependentAmountRelatedCall |  |
|------------------------|----------------------------------------|--|
| Expiry                 |                                        |  |
| Expiry                 | ExpiryDateTime                         |  |
| Expiry                 | Undertaking                            |  |
| Expiry                 | ExpiryCondition                        |  |
| Expiry                 | OpenEndedIndicator                     |  |
| Expiry                 | ExpiryPlace                            |  |
| ExposureCalculation    |                                        |  |
| ExposureCalculation    | TotalCollateralCurrentValue            |  |

| ExposureCalculation | TotalExposedAmount                 |  |
|---------------------|------------------------------------|--|
| ExposureCalculation | CurrentIndependentAmount           |  |
| ExposureCalculation | CurrentVariationMargin             |  |
| ExposureCalculation | CurrentSegregatedIndependentAmount |  |
| ExposureCalculation | VariationMarginAmountRequirement   |  |
| ExposureCalculation | SegregatedAmountRequirement        |  |
| ExposureCalculation | CollateralManagement               |  |
|                     |                                    |  |

| ExposureCalculation | CounterpartyRisk            |  |
|---------------------|-----------------------------|--|
| ExposureCalculation | TransactionRisk             |  |
| ExposureCalculation | TotalCollateralAfterHaircut |  |
| ExposureTerm        |                             |  |
| ExposureTerm        | ExposureType                |  |
| ExposureTerm        | MinimumTransferAmount       |  |
| ExposureTerm        | RoundingAmount              |  |

| ExposureTerm<br>RoundingMethod<br>ExposureTerm<br>RelatedCollateralAgreement<br>ExposureTerm<br>MinimumRequirementDeposit<br>FATCAStatus<br>FATCAStatus<br>FATCAStatus<br>FATCAStatus<br>FATCASourceStatus<br>FATCAStatus<br>InvestmentAccountParty |  |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                     |  |  |

| FATCAStatus             | FATCAReportingDate    |              | Date provided by the account<br>owner to inform the account<br>servicer of the date on which the<br>holdings must be reported before<br>the account is subsequently<br>closed. | ISODate           |                         |
|-------------------------|-----------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------------|
| FinancialDocument       |                       | Document     | Type of document used in<br>relation with financial<br>transactions.                                                                                                           |                   |                         |
| FinancialInstitution    |                       | Organisation | Organisation established<br>primarily to provide financial<br>services.                                                                                                        |                   |                         |
| FinancialInstitution    | RelatedPaymentTracker |              | Tracker identified by this agent.                                                                                                                                              | PaymentTracker    | Agent                   |
| FinancialInstrumentSwap |                       |              | Characteristics and conditions by<br>which a borrower can exchange<br>one type of financial instrument<br>for another.                                                         |                   |                         |
| FinancialInstrumentSwap | Maturity              |              | Range of time during which a<br>swap is in effect.                                                                                                                             | DateTimePeriod    | FinancialInstrumentSwap |
| FinancialInstrumentSwap | SpotSell              |              | Details of the spot leg of the sell<br>side of a swap.                                                                                                                         | SecuritiesSwapLeg | SpotSellSwap            |
| FinancialInstrumentSwap | SpotBuy               |              | Details of the spot leg of the buy<br>side of a swap.                                                                                                                          | SecuritiesSwapLeg | SpotBuySwap             |
| FinancialInstrumentSwap | ForwardBuyBack        |              | Details of the forward leg of a<br>swap that has been sold and is<br>being returned, ie, bought back.                                                                          | SecuritiesSwapLeg | ForwardBuyBackSwap      |
| FinancialInstrumentSwap | ForwardSellBack       |              | Details of the forward leg of a<br>swap that has been bought and<br>is being returned, ie, sold back.                                                                          | SecuritiesSwapLeg | ForwardSellBackSwap     |
| FinancialInstrumentSwap | RelatedQuote          |              | Quote related to a swap.                                                                                                                                                       | Quote             | QuoteSwap               |

| FinancialInstrumentSwap | ForwardSellBackFrequency    |         |
|-------------------------|-----------------------------|---------|
| FinancialInstrumentSwap | ForwardBuyBackFrequency     |         |
| FinancialInstrumentSwap | InterestComputation         |         |
| FinancialProduct        |                             | Product |
| FinancialService        |                             | Service |
| FinancialTransaction    |                             |         |
| FinancialTransaction    | CorporateActionDistribution |         |
| FinancialTransaction    | InterestManagement          |         |
| FinancialTransaction    | Trade                       |         |
| FinancialTransaction    | CollateralMovement          |         |
|                         |                             |         |

| FinancialTransaction   | BankingTransaction   |                           |
|------------------------|----------------------|---------------------------|
| FinancialTransaction   | RegulatoryReport     |                           |
| FinancingRequestorRole |                      | InvoiceFinancingPartyRole |
| FirstAgentRole         |                      | InvoiceFinancingPartyRole |
| FixingCondition        |                      |                           |
| FixingCondition        | FixingDateTime       |                           |
| FixingCondition        | NonDeliverableTrade  |                           |
| FixingCondition        | FixingRate           |                           |
| FixingCondition        | SettlementRateOption |                           |
|                        |                      |                           |

| FixingCondition      | FinancialCenter        |               |
|----------------------|------------------------|---------------|
| FixingCondition      | DisruptionFallback     |               |
| FixingCondition      | BusinessDayConvention  |               |
| ForeignExchangeSwap  |                        | TreasuryTrade |
| ForeignExchangeSwap  | LinkSwapIdentification |               |
| ForeignExchangeSwap  | SwapLeg                |               |
| ForeignExchangeTrade |                        | TreasuryTrade |
| ForeignExchangeTrade | AgreedRate             |               |

| ForeignExchangeTrade | TypeOfProduct                           |  |
|----------------------|-----------------------------------------|--|
| ForeignExchangeTrade | BuyAmount                               |  |
| ForeignExchangeTrade | SellAmount                              |  |
| ForeignExchangeTrade | ResultingSettlement                     |  |
| ForeignExchangeTrade | CurrencyExchangeForSecuritiesSettlement |  |
| ForeignExchangeTrade | OpeningLegRelatedNonDeliverableTrade    |  |
| ForeignExchangeTrade | ClosingLegRelatedNonDeliverableTrade    |  |
| ForeignExchangeTrade | RelatedSwap                             |  |
| ForeignExchangeTrade | RelatedOption                           |  |
| ForeignExchangeTrade | CurrencyExchangeForTaxVoucher           |  |
|                      |                                         |  |

| ForeignExchangeTrade  | ExchangeForwardPoint |                         |
|-----------------------|----------------------|-------------------------|
| ForeignExchangeTrade  | PostTradeEvent       |                         |
| ForwardingAgentRole   |                      | PaymentPartyRole        |
| FundAccountantRole    |                      | InvestmentFundPartyRole |
| FundAdministratorRole |                      | InvestmentFundPartyRole |

| FundManagerRole |                              | InvestmentFundPartyRole |
|-----------------|------------------------------|-------------------------|
| FundOrderDesk   |                              | InvestmentFundPartyRole |
| FundOrderDesk   | MainFundOrderDeskIndicator   |                         |
| FundOrderDesk   | MainFundOrderDeskAccount     |                         |
| FundPromoter    |                              | FundManagerRole         |
| FundsCashFlow   |                              |                         |
| FundsCashFlow   | ExceptionalCashFlowIndicator |                         |
|                 |                              |                         |

| FundsCashFlow | FlowDirection                |            |
|---------------|------------------------------|------------|
| FundsCashFlow | FundSubscriptionAccountEntry |            |
| FundsCashFlow | FundRedemptionAccountEntry   |            |
| FundsCashFlow | RelatedOrder                 |            |
| FundsCashFlow | NetIndicator                 |            |
| FundsCashFlow | NetAssetValueCalculation     |            |
| FundsCashFlow | CashFlowQuantity             |            |
| Future        |                              | Derivative |
| Future        | FutureDate                   |            |
| Future        | MinimumSize                  |            |
|               |                              |            |

| Future     | UnitOfMeasure           |  |
|------------|-------------------------|--|
| Future     | LastDeliveryDate        |  |
| Future     | Standardisation         |  |
| Future     | UnderlyingType          |  |
| Future     | FutureRule              |  |
| FutureRule |                         |  |
| FutureRule | TimeType                |  |
| FutureRule | RelatedFutureInstrument |  |
| FutureRule | MaximumTimeToMaturity   |  |
|            |                         |  |

| FutureRule            | MinimumTimeToMaturity         |                   |
|-----------------------|-------------------------------|-------------------|
| FutureRule            | BaseInterestRate              |                   |
| Garnishment           |                               | PaymentObligation |
| GenericIdentification |                               |                   |
| GenericIdentification | Identification                |                   |
| GenericIdentification | IdentificationForContactPoint |                   |
| GenericIdentification | IdentificationForAccount      |                   |
| GenericIdentification | RelatedPartyIdentification    |                   |
| GenericIdentification | IssueDate                     |                   |

| GenericIdentification | ExpiryDate                                   |  |
|-----------------------|----------------------------------------------|--|
| GenericIdentification | Scheme                                       |  |
| GenericIdentification | IdentificationForSecuritiesCertificate       |  |
| GenericIdentification | IdentificationForLot                         |  |
| GenericIdentification | PartyRole                                    |  |
| GenericIdentification | IdentificationForCashProceedsIncome          |  |
| GenericIdentification | RelatedStatusReason                          |  |
| GenericIdentification | IdentificationForBankTransaction             |  |
| GenericIdentification | IdentificationForAccountCostReferencePattern |  |
| GenericIdentification | Account                                      |  |
| GenericIdentification | RelatedSystemIdentification                  |  |
|                       |                                              |  |

| GenericIdentification | IdentificationForInterestName        |                     |
|-----------------------|--------------------------------------|---------------------|
| GenericIdentification | RelatedCashAccountService            |                     |
| GenericIdentification | IdentificationForInvestmentFundClass |                     |
| GenericIdentification | IdentifiedLocation                   |                     |
| GenericIdentification | RelatedSecuritiesIdentification      |                     |
| GenericIdentification | IdentifiedDocument                   |                     |
| GenericIdentification | RelatedPurchaseOrder                 |                     |
| GenericIdentification | RelatedCertificate                   |                     |
| GiveUpClearingFirm    |                                      | SettlementPartyRole |
| GiverRole             |                                      | CollateralPartyRole |
|                       |                                      |                     |

| Goods           |                         | Product |
|-----------------|-------------------------|---------|
| Goods           | Transport               |         |
| Goods           | Analysis                |         |
| Goods           | HealthCheck             |         |
| Goods           | PhytosanitaryInspection |         |
| Goods           | PartyRole               |         |
| GoodsPartyRole  |                         | Role    |
| GoodsPartyRole  | Item                    |         |
| GovernanceRules |                         |         |
| GovernanceRules | ModelForm               |         |
| GovernanceRules | Identification          |         |
|                 |                         |         |

| GovernanceRules | ApplicableLaw     |                         |
|-----------------|-------------------|-------------------------|
| GovernanceRules | Jurisdiction      |                         |
| GovernanceRules | PublicationAgency |                         |
| Grantor         |                   | InvestmentFundPartyRole |
| Guarantee       |                   | Asset                   |
| Guarantee       | CoveredAmount     |                         |
| Guarantee       | EffectivePeriod   |                         |
| Guarantee       | GuaranteeType     |                         |
| Guarantee       | CoveredPercentage |                         |
| Guarantee       | Document          |                         |
| Guarantee       | GuaranteedTrade   |                         |
| Guarantee       | ExcessAmount      |                         |
|                 |                   |                         |

| Guarantee            | GuaranteePartyRole |                    |
|----------------------|--------------------|--------------------|
| GuaranteeBeneficiary |                    | GuaranteePartyRole |
| GuaranteePartyRole   |                    | Role               |
| GuaranteePartyRole   | Guarantee          |                    |
| GuarantorRole        |                    | GuaranteePartyRole |
| GuarantorRole        | Position           |                    |
| HaircutValuation     |                    |                    |
| HaircutValuation     | AssetHolding       |                    |
| HaircutValuation     | Haircut            |                    |
| HaircutValuation     | Sign               |                    |
| HaircutValuation     | PartyRole          |                    |
|                      |                    |                    |

| Household                |               |                      |
|--------------------------|---------------|----------------------|
| Household                | Member        |                      |
| IdentificationIssuerRole |               | InformationPartyRole |
| IdentificationIssuerRole | Country       |                      |
| IdentificationIssuerRole | EntityName    |                      |
| IdentificationIssuerRole | OwnerCode     |                      |
| IncentivePremium         |               |                      |
| IncentivePremium         | PerSecurity   |                      |
| IncentivePremium         | PerVote       |                      |
| IncentivePremium         | PerAttendee   |                      |
| IncentivePremium         | Description   |                      |
| IncentivePremium         | PremiumAmount |                      |

| IncentivePremium | PaymentDate                 |  |
|------------------|-----------------------------|--|
| IncentivePremium | Meeting                     |  |
| IncentivePremium | CorporateActionDistribution |  |
|                  |                             |  |
|                  |                             |  |
| Incoterms        |                             |  |
|                  |                             |  |
|                  |                             |  |
|                  |                             |  |
| Incoterms        | Transport                   |  |
| Incoterms        | Code                        |  |
| Incoterms        | Location                    |  |
|                  |                             |  |

| IndependentAmount     |                                  |              |
|-----------------------|----------------------------------|--------------|
| IndependentAmount     | RelatedRiskCalculation           |              |
| IndependentAmount     | IndependentAmountPerTrade        |              |
| IndependentAmount     | IndependentAmountValueAtRisk     |              |
| IndependentAmount     | IndependentAmountNetOpenPosition |              |
| IndependentAmountTerm |                                  | ExposureTerm |

| IndependentAmountTerm | Convention      |  |
|-----------------------|-----------------|--|
| Index                 |                 |  |
| Index                 | IndexRateBasis  |  |
| Index                 | IndexFactor     |  |
| Index                 | IndexPoints     |  |
| Index                 | IndexFixingDate |  |
| Index                 | Identification  |  |
| Index                 | ReferenceSource |  |
|                       |                 |  |

| Index              | IndexRateCurrency   |                            |
|--------------------|---------------------|----------------------------|
| Index              | IndexRateFrequency  |                            |
| Index              | IndexRateMultiplier |                            |
| Index              | Spread              |                            |
| Index              | PortfolioBenchmark  |                            |
| Index              | VariableInterest    |                            |
| Index              | SecuritiesPricing   |                            |
| IndirectMember     |                     | ThirdPartyRole             |
| IndividualInvestor |                     | InvestmentAccountPartyRole |
| IndividualPayment  |                     | Payment                    |
| IndividualPayment  | BulkPayment         |                            |

| InformationPartyRole |                           | Role |
|----------------------|---------------------------|------|
| InformationPartyRole | GenericIdentification     |      |
| InformationPartyRole | HaircutValuation          |      |
| InformationPartyRole | Price                     |      |
| InformationPartyRole | Scheme                    |      |
| InformationPartyRole | Quote                     |      |
| InformationPartyRole | TreasuryTrade             |      |
| InformationQualifier |                           |      |
| InformationQualifier | SystemBusinessInformation |      |
| InformationQualifier | IsFormatted               |      |
| InformationQualifier | Priority                  |      |

| InitiatingPartyRole<br>PaymentPartyRole<br>Instalment<br>PaymentObligation<br>Instalment<br>InitialNumberOfInstalment<br>Instalment<br>TotalNumberOfInstalment<br>Instalment<br>PeriodUnit<br>Instalment<br>NumberOfUnits<br>Instalment<br>SequenceIdentification<br>Instalment<br>InvestmentPlan |  |  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                   |  |  |

| Instalment                   | InstalmentPlanType |                                    |
|------------------------------|--------------------|------------------------------------|
| Instalment                   | FirstPaymentAmount |                                    |
| Instalment                   | FirstPaymentDate   |                                    |
| InstructedAgentRole          |                    | PaymentPartyRole                   |
| InstructedReimbursementAgent |                    | CashSettlementInstructionPartyRole |
| InstructingAgentRole         |                    | PaymentPartyRole                   |
| InstructingAgentRole         | Previous           |                                    |

| InstructingReimbursementAgent |                        | CashSettlementInstructionPartyRole |
|-------------------------------|------------------------|------------------------------------|
| InstructionForMeeting         |                        |                                    |
| InstructionForMeeting         | VoteInstruction        |                                    |
| InstructionForMeeting         | RequestedExecutionDate |                                    |
| InstructionForMeeting         | RelatedServicing       |                                    |
| InstructionForMeeting         | MeetingAttendance      |                                    |
| InstructionForMeeting         | ProxyAppointment       |                                    |
| InstructionForMeeting         | MeetingIdentification  |                                    |
| InstructionForMeeting         | SecuritiesRegistration |                                    |
|                               |                        |                                    |

| InstructionForMeeting | BlockingSecurities        |          |
|-----------------------|---------------------------|----------|
| InstructionForMeeting | ParticipationRegistration |          |
| InstructionForMeeting | SafekeepingAccount        |          |
| InsuranceCertificate  |                           | Document |
| InsuranceCertificate  | EffectiveDate             |          |
| InsuranceCertificate  | InsuredAmount             |          |
| InsuranceCertificate  | InsuranceConditions       |          |
| InsuranceCertificate  | InsuranceClauses          |          |
| InsuranceCertificate  | ClaimsPayableAt           |          |
| InsuranceCertificate  | ClaimsPayableIn           |          |
| InsuranceCertificate  | InsurancePartyRole        |          |
|                       |                           |          |

| InsuranceCertificate | ProductDelivery       |                    |
|----------------------|-----------------------|--------------------|
| InsuranceCertificate | InsuranceType         |                    |
| InsuranceCertificate | RelatedInvestmentPlan |                    |
| InsurancePartyRole   |                       | Role               |
| InsurancePartyRole   | InsuranceCertificate  |                    |
| Insurer              |                       | InsurancePartyRole |
|                      |                       |                    |
| Interest             |                       |                    |
|                      |                       |                    |
| Interest             | AccruedInterestAmount |                    |
|                      |                       |                    |
| Interest             | InterestCalculation   |                    |
| Interest             | Amount                |                    |
| Interest             | Rate                  |                    |
|                      |                       |                    |

| Interest | RelatedCashProceedsDefinition | Cash proceeds definition for<br>which an interest is provided.                                                                                 |
|----------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Interest | SecuritiesFinancing           | Specifies the financing trade on<br>which this interest apply.                                                                                 |
| Interest | InterestTax                   | Specifies the tax on interest.                                                                                                                 |
| Interest | CreditDebitIndicator          | Indicates whether the interest is<br>a debit or credit.                                                                                        |
| Interest | CashEntry                     | Entry which contains the interest.                                                                                                             |
| Interest | PaymentDate                   | Date of the next interest<br>payment.                                                                                                          |
| Interest | RelatedInterestManagement     | Management of interest which<br>consists into calculating the<br>interest, requesting its payment<br>or distributing the interest<br>proceeds. |
| Interest | RelatedUndertakingAmount      | Undertaking amount for which an<br>interest is specified.                                                                                      |
| Interest | RelatedDebitCreditFacility    | Debit and credit facilities on<br>which the interest applies.                                                                                  |
| Interest | SecuritiesSettlement          | Securities settlement process for<br>which an accrued interest is<br>specified.                                                                |
| Interest | InterestName                  | Interest rate expressed as a rate<br>name.                                                                                                     |
| Interest | RelatedAssetHolding           | Asset holding on which interest is<br>paid.                                                                                                    |
| Interest | Deposit                       | Deposit for which an interest is<br>Deposit<br>specified.                                                                                      |
|          |                               |                                                                                                                                                |

| Interest            | AccountBalance                  |  |
|---------------------|---------------------------------|--|
| Interest            | RelatedAccountContract          |  |
| Interest            | RelatedNetAssetValueCalculation |  |
| Interest            | TypeOfInterest                  |  |
| Interest            | RelatedPaymentCard              |  |
| InterestCalculation |                                 |  |
| InterestCalculation | DayCountBasis                   |  |
| InterestCalculation | Rate                            |  |
| InterestCalculation | Interest                        |  |
| InterestCalculation | RateType                        |  |

| InterestCalculation | InterestPeriod       | Period during which the interest<br>DateTimePeriod<br>rate has been applied.                                                                                                                                                   |
|---------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InterestCalculation | RelatedIndex         | Index rate related to the interest<br>rate of the forthcoming interest<br>PercentageRate<br>payment.                                                                                                                           |
| InterestCalculation | InterestAccrualDate  | Start date used for calculating<br>accrued interest on debt<br>instruments which are being sold<br>between interest payment dates.<br>ISODateTime<br>Often but not always the same as<br>the issue date and the dated<br>date. |
| InterestCalculation | CalculationMethod    | Specifies whether the interest is<br>CalculationMethodCode<br>simple or compounded.                                                                                                                                            |
| InterestCalculation | VariableInterest     | Specifies the parameters to be<br>used for variable interest<br>VariableInterest<br>payments.                                                                                                                                  |
| InterestCalculation | InterestType         | Specifies the type of interest.<br>InterestCode                                                                                                                                                                                |
| InterestCalculation | RateValidityRange    | Specifies the amount range for<br>which the interest rate is<br>AmountRange<br>applicable.                                                                                                                                     |
| InterestCalculation | InterestMethod       | Indicates whether the interest<br>will be settled in cash or rolled in<br>InterestMethodCode<br>the existing collateral balance.                                                                                               |
| InterestCalculation | CalculationFrequency | Specifies the periodicity of the<br>FrequencyCode<br>calculation of the interest.                                                                                                                                              |
| InterestCalculation | CalculationDate      | Indicates the calculation date of<br>ISODate<br>the interest amount.                                                                                                                                                           |
| InterestCalculation | Charges              | Specifies the charges on interest.<br>Charges                                                                                                                                                                                  |

| InterestCalculation   | DebtInstrument            |                  |
|-----------------------|---------------------------|------------------|
| InterestCalculation   | Spread                    |                  |
| InterestCalculation   | PaymentFrequency          |                  |
| InterestCalculation   | RelatedInterestManagement |                  |
| InterestManagement    |                           |                  |
| InterestManagement    | InterestCalculation       |                  |
| InterestManagement    | FinancialTransaction      |                  |
| InterestManagement    | Interest                  |                  |
| InterestManagement    | PaymentObligation         |                  |
| IntermediaryAgentRole |                           | PaymentPartyRole |
|                       |                           |                  |

| IntermediaryAgentRole | IntermediaryAgentRole |                           |
|-----------------------|-----------------------|---------------------------|
| IntermediaryAgentRole | NextParty             |                           |
| IntermediaryAgentRole | Position              |                           |
| IntermediaryRole      |                       | AccountPartyRole          |
| IntermediateAgentRole |                       | InvoiceFinancingPartyRole |
| IntraPositionTransfer |                       | SecuritiesTransfer        |
| IntraPositionTransfer | Reservation           |                           |
| IntraPositionTransfer | CollateralAmount      |                           |
| IntraPositionTransfer | SecuritiesBalance     |                           |
|                       |                       |                           |

| InvestigationCase<br>InvestigationCase<br>AssignmentIdentification<br>InvestigationCase<br>CreationDateTime<br>InvestigationCase<br>Identification<br>InvestigationCase<br>Status<br>InvestigationCase<br>InvestigationPartyRole<br>InvestigationCase<br>DuplicateCaseResolution<br>InvestigationCase<br>InvestigationResolution<br>InvestigationCase<br>OriginalInvestigationCase | IntroducingFirm | SecuritiesOrderPartyRole |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|--------------------------|
|                                                                                                                                                                                                                                                                                                                                                                                    |                 |                          |
|                                                                                                                                                                                                                                                                                                                                                                                    |                 |                          |
|                                                                                                                                                                                                                                                                                                                                                                                    |                 |                          |
|                                                                                                                                                                                                                                                                                                                                                                                    |                 |                          |
|                                                                                                                                                                                                                                                                                                                                                                                    |                 |                          |
|                                                                                                                                                                                                                                                                                                                                                                                    |                 |                          |
|                                                                                                                                                                                                                                                                                                                                                                                    |                 |                          |
|                                                                                                                                                                                                                                                                                                                                                                                    |                 |                          |
|                                                                                                                                                                                                                                                                                                                                                                                    |                 |                          |

| InvestigationCase       | LinkedCase                           |        |
|-------------------------|--------------------------------------|--------|
| InvestigationCase       | Reassignment                         |        |
| InvestigationCase       | EIR                                  |        |
| InvestigationCase       | RequestorInvestigationIdentification |        |
| InvestigationCase       | InvestigationSubType                 |        |
| InvestigationCase       | InvestigationType                    |        |
| InvestigationCase       | ResponderInvestigationIdentification |        |
| InvestigationCaseStatus |                                      | Status |
| InvestigationCaseStatus | CaseStatus                           |        |

| InvestigationCaseStatus | InvestigationCase          |         |
|-------------------------|----------------------------|---------|
| InvestigationPartyRole  |                            | Role    |
| InvestigationPartyRole  | InvestigationCase          |         |
| InvestigationPartyRole  | Status                     |         |
| InvestigationResolution |                            |         |
| InvestigationResolution | InvestigationCase          |         |
| InvestigationResolution | InvestigationCaseReference |         |
| InvestmentAccount       |                            | Account |
| InvestmentAccount       | InvestmentAccountType      |         |
| InvestmentAccount       | OwnershipType              |         |
|                         |                            |         |

| InvestmentAccount | Designation               |  |
|-------------------|---------------------------|--|
| InvestmentAccount | ReferenceCurrency         |  |
| InvestmentAccount | InvestmentFundClass       |  |
| InvestmentAccount | CashAccount               |  |
| InvestmentAccount | SecuritiesAccount         |  |
| InvestmentAccount | InvestmentFundTax         |  |
| InvestmentAccount | InvestmentFundTransaction |  |
| InvestmentAccount | SidePocket                |  |
|                   |                           |  |

| InvestmentAccount         | InvestmentAccountPartyRole         |
|---------------------------|------------------------------------|
| InvestmentAccount         | DebitPortfolioTransfer             |
| InvestmentAccount         | CreditPortfolioTransfer            |
| InvestmentAccount         | AccountForInvestmentFundProcessing |
| InvestmentAccount         | InvestmentAccountContract          |
| InvestmentAccount         | AccountUsageType                   |
| InvestmentAccount         | Category                           |
| InvestmentAccount         | Portfolio                          |
| InvestmentAccount         | RelatedPortfolioTransfer           |
| InvestmentAccount         | UsufructPercentage                 |
| InvestmentAccount         | OwnershipPercentage                |
| InvestmentAccountContract | AccountContract                    |

| InvestmentAccountContract  | LetterIntentReference      |                  |
|----------------------------|----------------------------|------------------|
| InvestmentAccountContract  | AccumulationRightReference |                  |
| InvestmentAccountContract  | InvestmentAccount          |                  |
| InvestmentAccountContract  | Services                   |                  |
| InvestmentAccountContract  | ModeledAccount             |                  |
| InvestmentAccountPartyRole |                            | AccountPartyRole |
|                            |                            |                  |

| InvestmentAccountPartyRole | OwnershipBeneficiaryRate |                |
|----------------------------|--------------------------|----------------|
| InvestmentAccountPartyRole | InvestmentAccount        |                |
| InvestmentAccountPartyRole | FATCAFormType            |                |
| InvestmentAccountPartyRole | FATCAStatus              |                |
| InvestmentAccountPartyRole | CRSStatus                |                |
| InvestmentAccountService   |                          | AccountService |
| InvestmentAccountService   | IncomePreference         |                |

| InvestmentAccountService<br>RoundingMethod<br>InvestmentAccountService<br>BeneficiaryCertificationIndicator<br>InvestmentAccountService<br>BeneficiaryCertificationCompletion<br>InvestmentAccountService<br>SystematicInvestmentPlan<br>InvestmentAccountService<br>InvestmentAccountContract<br>InvestmentAccountService<br>ReportingService<br>InvestmentAccountService<br>Reinvestment<br>InvestmentAdvisor<br>AssetPartyRole | InvestmentAccountService | TaxWithholdingMethod |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|----------------------|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |                          |                      |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |                          |                      |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |                          |                      |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |                          |                      |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |                          |                      |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |                          |                      |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |                          |                      |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |                          |                      |  |

| InvestmentDecisionPerson |                      | SecuritiesOrderPartyRole | Identification of the person or<br>the algorithm within the member<br>or participant of the trading<br>venue who is responsible for the<br>investment decision.                                |  |
|--------------------------|----------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| InvestmentFund           |                      | FinancialProduct         | Distinct pool of financial<br>instruments managed by a single<br>investment policy. May or not be<br>part of an umbrella fund. The<br>pool is issued in at least one<br>investment fund class. |  |
| InvestmentFund           | DomicileCountry      |                          | Country in which the investment<br>Country<br>fund is domiciled.                                                                                                                               |  |
| InvestmentFund           | OrderDesk            |                          | Entity appointed by the fund, to<br>which orders should be<br>ContactPoint<br>submitted.                                                                                                       |  |
| InvestmentFund           | InvestmentFundClass  |                          | Sub-set of an investment fund.<br>InvestmentFundClass                                                                                                                                          |  |
| InvestmentFund           | FundType             |                          | Legal form of the fund, eg,<br>UCITS, SICAV, OEIC, Unit Trust,<br>Max35Text<br>and FCP.                                                                                                        |  |
| InvestmentFund           | TreasuryTradingParty |                          | Party which executes a treasury<br>trade on behalf of an investment<br>TreasuryTradingParty<br>fund.                                                                                           |  |
| InvestmentFund           | Identification       |                          | Identification of the investment<br>AnyBICDec2014Identifier<br>fund.                                                                                                                           |  |
| InvestmentFund           | Custodian            |                          | Party which settles the trades for<br>CustodianRole<br>the account of the fund.                                                                                                                |  |
| InvestmentFund           | PartyRole            |                          | Specifies each role linked to an<br>investment fund and played by a<br>InvestmentFundPartyRole<br>party in that context.                                                                       |  |
|                          |                      |                          |                                                                                                                                                                                                |  |

| InvestmentFund      | Family                     |          |
|---------------------|----------------------------|----------|
| InvestmentFund      | Structure                  |          |
| InvestmentFund      | LegalForm                  |          |
| InvestmentFund      | SubFundIndicator           |          |
| InvestmentFund      | EndOfFiscalYear            |          |
| InvestmentFund      | AccountingYearEndDate      |          |
| InvestmentFund      | FirstAccountingYearEndDate |          |
| InvestmentFund      | UmbrellaFund               |          |
| InvestmentFund      | AuthorisedCountry          |          |
| InvestmentFundClass |                            | Security |
|                     |                            |          |

| InvestmentFundClass | ClassType                |  |
|---------------------|--------------------------|--|
| InvestmentFundClass | DistributionPolicy       |  |
| InvestmentFundClass | DividendPolicy           |  |
| InvestmentFundClass | DualFundIndicator        |  |
| InvestmentFundClass | RequestedNAVCurrency     |  |
| InvestmentFundClass | TradingCurrency          |  |
| InvestmentFundClass | InvestmentFund           |  |
| InvestmentFundClass | PhysicalBearerSecurities |  |
|                     |                          |  |

| InvestmentFundClass<br>DematerialisedBearerSecurities<br>InvestmentFundClass<br>PhysicalRegisteredSecurities<br>InvestmentFundClass<br>DematerialisedRegisteredSecurities<br>InvestmentFundClass<br>ProcessingCharacteristics<br>InvestmentFundClass<br>ProductGroup<br>InvestmentFundClass<br>InvestmentAccount<br>InvestmentFundClass<br>NetAssetValueCalculation<br>InvestmentFundClass<br>InvestmentFundTransaction<br>InvestmentFundClass<br>SeriesIssueIdentificationDate |  |  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |

| InvestmentFundClass | SeriesName          | redemption or order<br>known. | Identifies the name of a fund<br>series. Typically applicable to a<br>confirmation, but may be<br>specified in the subscription, if    | Max35Text                          |  |                                      |
|---------------------|---------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|--|--------------------------------------|
| InvestmentFundClass | NewIssueIndicator   |                               | Indicates that the financial<br>instrument and/or series included<br>in the message is a new issue.                                    | YesNoIndicator                     |  |                                      |
| InvestmentFundClass | Equalisation        | the fiscal year.              | Part of an investor's subscription<br>amount that is held by the fund<br>in order to pay incentive /<br>performance fees at the end of | Equalisation                       |  | RelatedInvestmentFundTransaction     |
| InvestmentFundClass | TopUpAmount         | amount.                       | Additional amount of money<br>(top-up amount) required to<br>meet the minimum subscription                                             | CurrencyAndAmount                  |  |                                      |
| InvestmentFundClass | HoldBackAmount      | subject to hold back.         | Value of the redemption amount                                                                                                         | CurrencyAndAmount                  |  |                                      |
| InvestmentFundClass | HoldBackReleaseDate |                               | Date on which the hold back<br>amount is to be released.                                                                               | ISODate                            |  |                                      |
| InvestmentFundClass | LotDescription      | Description of the lot.       |                                                                                                                                        | Max350Text                         |  |                                      |
| InvestmentFundClass | FundClassification  |                               | Method of classifying a fund.                                                                                                          | GenericIdentification              |  | IdentificationForInvestmentFundClass |
| InvestmentFundClass | UnderlyingAssetType | which the fund invests.       | Specifies the type of assets in                                                                                                        | FinancialInstrumentProductTypeCode |  |                                      |
| InvestmentFundClass | InvestorType        | in the fund class.            | Type of investor that can invest                                                                                                       | InvestorTypeCode                   |  |                                      |
|                     |                     |                               |                                                                                                                                        |                                    |  |                                      |

| InvestmentFundClass                          | Reinvestment              |  |
|----------------------------------------------|---------------------------|--|
| InvestmentFundClass                          | OutstandingUnits          |  |
| InvestmentFundClass                          | FundEndDate               |  |
| InvestmentFundClassProcessingCharacteristics |                           |  |
| InvestmentFundClassProcessingCharacteristics | ReinvestmentFrequency     |  |
| InvestmentFundClassProcessingCharacteristics | FrontEndLoadIndicator     |  |
| InvestmentFundClassProcessingCharacteristics | BackEndLoadIndicator      |  |
| InvestmentFundClassProcessingCharacteristics | SwitchingFeeIndicator     |  |
| InvestmentFundClassProcessingCharacteristics | LimitedSubscriptionPeriod |  |
| InvestmentFundClassProcessingCharacteristics | LimitedRedemptionPeriod   |  |
|                                              |                           |  |

| InvestmentFundClassProcessingCharacteristics | Decimalisation               |  |
|----------------------------------------------|------------------------------|--|
| InvestmentFundClassProcessingCharacteristics | HoldingTransferableIndicator |  |
| InvestmentFundClassProcessingCharacteristics | ApplicationForm              |  |
| InvestmentFundClassProcessingCharacteristics | SignatureRequired            |  |
| InvestmentFundClassProcessingCharacteristics | AmountIndicator              |  |
| InvestmentFundClassProcessingCharacteristics | UnitsIndicator               |  |
| InvestmentFundClassProcessingCharacteristics | OrderCutOffDateTime          |  |
| InvestmentFundClassProcessingCharacteristics | SettlementCycle              |  |

| InvestmentFundClassProcessingCharacteristics | FundClass                             |  |
|----------------------------------------------|---------------------------------------|--|
| InvestmentFundClassProcessingCharacteristics | HoldingTransferable                   |  |
| InvestmentFundClassProcessingCharacteristics | DealingFrequency                      |  |
| InvestmentFundClassProcessingCharacteristics | LimitedPeriod                         |  |
| InvestmentFundClassProcessingCharacteristics | SettlementAccount                     |  |
| InvestmentFundClassProcessingCharacteristics | Country                               |  |
| InvestmentFundClassProcessingCharacteristics | LocalMarketAnnex                      |  |
| InvestmentFundClassProcessingCharacteristics | EffectiveDate                         |  |
| InvestmentFundClassProcessingCharacteristics | SubsequentSubscriptionApplicationForm |  |

| InvestmentFundClassProcessingCharacteristics | RedemptionForm                  |  |
|----------------------------------------------|---------------------------------|--|
| InvestmentFundClassProcessingCharacteristics | DealingCurrency                 |  |
| InvestmentFundClassProcessingCharacteristics | DealingCutOffTimeFrame          |  |
| InvestmentFundClassProcessingCharacteristics | MinimumHoldingAmount            |  |
| InvestmentFundClassProcessingCharacteristics | MaximumRedemptionUnits          |  |
| InvestmentFundClassProcessingCharacteristics | MinimumHoldingUnits             |  |
| InvestmentFundClassProcessingCharacteristics | MinimumRemainingHoldingAmount   |  |
| InvestmentFundClassProcessingCharacteristics | MaximumRedemptionPercentage     |  |
| InvestmentFundClassProcessingCharacteristics | MaximumRedemptionAmount         |  |
| InvestmentFundClassProcessingCharacteristics | MinimumInitialSubscriptionUnits |  |
| InvestmentFundClassProcessingCharacteristics | MinimumSubscriptionAmount       |  |

| InvestmentFundClassProcessingCharacteristics | MinimumInitialSubscriptionAmount |                 |
|----------------------------------------------|----------------------------------|-----------------|
| InvestmentFundClassProcessingCharacteristics | MinimumSubscriptionUnits         |                 |
| InvestmentFundClassProcessingCharacteristics | MinimumHoldingPeriod             |                 |
| InvestmentFundClassProcessingCharacteristics | MinimumRedemptionPercentage      |                 |
| InvestmentFundFamily                         |                                  |                 |
| InvestmentFundFamily                         | FundFamilyName                   |                 |
| InvestmentFundFamily                         | InvestmentFund                   |                 |
| InvestmentFundOrder                          |                                  | SecuritiesOrder |
|                                              |                                  |                 |

| InvestmentFundOrder<br>GrossAmountIndicator         |
|-----------------------------------------------------|
| InvestmentFundOrder<br>RelatedTransaction           |
| InvestmentFundOrder<br>OrderType                    |
| InvestmentFundOrder<br>GrossAmount                  |
| InvestmentFundOrder<br>UnitsNumber                  |
| InvestmentFundOrder<br>InvestmentFundOrderExecution |
| InvestmentFundOrder<br>NetAmount                    |
| InvestmentFundOrder<br>OrderDateTime                |

| InvestmentFundOrder | ExpiryDateTime              |  |
|---------------------|-----------------------------|--|
| InvestmentFundOrder | CancellationRight           |  |
| InvestmentFundOrder | RequestedSettlementCurrency |  |
| InvestmentFundOrder | RequestedExecutionDateTime  |  |
| InvestmentFundOrder | FinancialAdvice             |  |
| InvestmentFundOrder | NegotiatedTrade             |  |
| InvestmentFundOrder | HoldingsRate                |  |
| InvestmentFundOrder | OrderWaiverReason           |  |
| InvestmentFundOrder | InitialOrderIndicator       |  |
| InvestmentFundOrder | OrderBookingDate            |  |

| InvestmentFundOrder          | InvestmentPlan                   |                          |
|------------------------------|----------------------------------|--------------------------|
| InvestmentFundOrder          | OrderStatus                      |                          |
| InvestmentFundOrder          | TotalAmount                      |                          |
| InvestmentFundOrderExecution |                                  | SecuritiesTradeExecution |
| InvestmentFundOrderExecution | UnitsNumber                      |                          |
| InvestmentFundOrderExecution | NonStandardSettlementInformation |                          |
| InvestmentFundOrderExecution | Order                            |                          |
| InvestmentFundOrderExecution | DealIdentification               |                          |
| InvestmentFundOrderExecution | ExecutedTradePrice               |                          |
| InvestmentFundOrderExecution | PartiallyExecutedIndicator       |                          |

| InvestmentFundOrderExecution | InterimProfitAmount       | Part of the price deemed as<br>accrued income or profit rather<br>than capital. The interim profit<br>amount is used for tax purposes. | CurrencyAndAmount         |                                    |
|------------------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------|
| InvestmentFundOrderExecution | InformativePrice          | Other quoted price than the one<br>at which the order was executed.                                                                    | SecuritiesPricing         | FundOrderRelatedToInformativePrice |
| InvestmentFundOrderExecution | BestExecution             | Specifies that the execution was<br>subject to best execution rules as<br>defined by MiFID.                                            | BestExecutionCode         |                                    |
| InvestmentFundOrderExecution | PartialSettlementOfUnits  | Percentage of units partially<br>settled.                                                                                              | PercentageRate            |                                    |
| InvestmentFundOrderExecution | PartialSettlementOfCash   | Percentage of cash partially<br>settled.                                                                                               | PercentageRate            |                                    |
| InvestmentFundOrderExecution | LateReport                | Specifies whether the order<br>execution confirmation is late.                                                                         | LateReportCode            |                                    |
| InvestmentFundOrderExecution | SettledIndicator          | Indicates whether the cash<br>payment with respect to the<br>executed order is settled.                                                | YesNoIndicator            |                                    |
| InvestmentFundOrderExecution | RegisteredIndicator       | Indicates whether the executed<br>order has a registered status on<br>the books of the transfer agent.                                 | YesNoIndicator            |                                    |
| InvestmentFundOrderExecution | ExecutedAmount            | Amount of money invested or<br>redeemed as a result of an<br>investment fund order.                                                    | CurrencyAndAmount         |                                    |
| InvestmentFundOrderExecution | InvestmentFundTransaction | Transaction which is executed.                                                                                                         | InvestmentFundTransaction | InvestmentFundOrderExecution       |
| InvestmentFundOrderExecution | CashFlow                  | Specifies the cash flow resulting<br>from the execution of an order.                                                                   | FundsCashFlow             | RelatedOrder                       |
| InvestmentFundOrderExecution | SourceOfCash              | Source of cash used for the<br>settlement of the execution.                                                                            | SourceOfCashCode          |                                    |
|                              |                           |                                                                                                                                        |                           |                                    |

| InvestmentFundPartyRole<br>Role<br>InvestmentFundPartyRole<br>Account<br>InvestmentFundPartyRole<br>InvestmentFund<br>InvestmentFundTax<br>SecuritiesTax<br>InvestmentFundTax<br>FiscalExemption<br>InvestmentFundTax<br>InvestmentAccount<br>InvestmentFundTax<br>PercentageOfDebtClaim<br>InvestmentFundTax<br>PercentageGrandfatheredDebt<br>InvestmentFundTax<br>ExemptionIndicator |  |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                         |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                         |  |  |

| InvestmentFundTax         | Transaction          |                 |
|---------------------------|----------------------|-----------------|
| InvestmentFundTransaction |                      | SecuritiesTrade |
| InvestmentFundTransaction | InvestmentFundOrder  |                 |
| InvestmentFundTransaction | ClientReference      |                 |
| InvestmentFundTransaction | Type                 |                 |
| InvestmentFundTransaction | TransactionCharge    |                 |
| InvestmentFundTransaction | InvestmentAccount    |                 |
| InvestmentFundTransaction | InvestmentFundClass  |                 |
| InvestmentFundTransaction | TransactionTax       |                 |
| InvestmentFundTransaction | CreditDebitIndicator |                 |
|                           |                      |                 |

| InvestmentFundTransaction | InvestmentFundOrderExecution |  |
|---------------------------|------------------------------|--|
| InvestmentPlan            |                              |  |
| InvestmentPlan            | Frequency                    |  |
| InvestmentPlan            | Amount                       |  |
| InvestmentPlan            | Asset                        |  |
| InvestmentPlan            | Instalment                   |  |
| InvestmentPlan            | RelatedService               |  |
| InvestmentPlan            | Insurance                    |  |
| InvestmentPlan            | StandingOrder                |  |
|                           |                              |  |

| InvestmentPlan | MultiCurrency       |                            |
|----------------|---------------------|----------------------------|
| InvestmentPlan | Currency            |                            |
| InvestmentPlan | Portfolio           |                            |
| InvestmentPlan | InvestmentPeriod    |                            |
| InvestmentPlan | PlanStatus          |                            |
| InvestmentPlan | Pension             |                            |
| InvestmentPlan | TaxEfficientProduct |                            |
| Investor       |                     | InvestmentAccountPartyRole |
| Investor       | NewIssuePermission  |                            |
| Investor       | DeMinimusApplicable |                            |
| Investor       | Restricted          |                            |

| Investor     | RestrictedPersonReason                  |                   |
|--------------|-----------------------------------------|-------------------|
| InvestorRole |                                         | TradePartyRole    |
| InvestorRole | IndividualInvestor                      |                   |
| InvestorRole | CorporateInvestor                       |                   |
| InvestorRole | Capacity                                |                   |
| InvestorRole | InvestorProtectionAssociationMembership |                   |
| InvestorRole | Type                                    |                   |
| Invoice      |                                         | FinancialDocument |
| Invoice      | CreditDebitNoteAmount                   |                   |
| Invoice      | TotalTaxAmount                          |                   |

| Invoice | TotalInvoiceAmount      |  |
|---------|-------------------------|--|
| Invoice | InvoiceCurrency         |  |
| Invoice | PeriodCovered           |  |
| Invoice | TradeSettlement         |  |
| Invoice | TotalCharge             |  |
| Invoice | TotalPrepaidAmount      |  |
| Invoice | LineItem                |  |
| Invoice | TotalNetAmount          |  |
| Invoice | CurrencyExchange        |  |
| Invoice | BillingCompensationType |  |
|         |                         |  |

| Invoice | InvoicePartyRole                          |  |
|---------|-------------------------------------------|--|
| Invoice | OriginalInvoice                           |  |
| Invoice | RelatedInvoice                            |  |
| Invoice | InvoiceFinancingTransaction               |  |
| Invoice | BillingCompensationAmount                 |  |
| Invoice | InvoiceStatus                             |  |
| Invoice | Payment                                   |  |
| Invoice | CreditDebitIndicator                      |  |
| Invoice | LimitedPresentmentIndicator               |  |
| Invoice | RelatedElectronicInvoiceProcessingService |  |
| Invoice | ActivationRequestDeliveryParty            |  |
|         |                                           |  |

| InvoiceFinancingAgreement |                     | Agreement |
|---------------------------|---------------------|-----------|
| InvoiceFinancingAgreement | Authorisation       |           |
| InvoiceFinancingAgreement | FinancingMethod     |           |
| InvoiceFinancingAgreement | RequestedAmount     |           |
| InvoiceFinancingAgreement | RequestedPercentage |           |
| InvoiceFinancingAgreement | AppliedPercentage   |           |

| InvoiceFinancingAgreement | FinancedAmount              |                  |
|---------------------------|-----------------------------|------------------|
| InvoiceFinancingAgreement | Identification              |                  |
| InvoiceFinancingAgreement | InvoiceFinancingPartyRole   |                  |
| InvoiceFinancingAgreement | InvoiceFinancingStatus      |                  |
| InvoiceFinancingAgreement | Invoice                     |                  |
| InvoiceFinancingAgreement | ResultingCashEntry          |                  |
| InvoiceFinancingAgreement | Assignment                  |                  |
| InvoiceFinancingPartyRole |                             | InvoicePartyRole |
| InvoiceFinancingPartyRole | CashAccount                 |                  |
| InvoiceFinancingPartyRole | InvoiceFinancingTransaction |                  |
| InvoiceFinancingStatus    |                             | Status           |
|                           |                             |                  |

| InvoiceFinancingStatus | ValidationStatusReason      |        |
|------------------------|-----------------------------|--------|
| InvoiceFinancingStatus | ValidationStatus            |        |
| InvoiceFinancingStatus | CancellationStatus          |        |
| InvoiceFinancingStatus | CancellationStatusReason    |        |
| InvoiceFinancingStatus | FinancingTransactionStatus  |        |
| InvoiceFinancingStatus | CancellationRequestReason   |        |
| InvoiceFinancingStatus | InvoiceFinancingTransaction |        |
| InvoiceFinancingStatus | FinancingStatusReason       |        |
| InvoicePartyRole       |                             | Role   |
| InvoicePartyRole       | Invoice                     |        |
| InvoiceStatus          |                             | Status |

| InvoiceStatus | Invoice                |                  |
|---------------|------------------------|------------------|
| InvoiceeRole  |                        | InvoicePartyRole |
| InvoicerRole  |                        | InvoicePartyRole |
| Issuance      |                        |                  |
| Issuance      | IssueDate              |                  |
| Issuance      | IssueDiscountAllowance |                  |
| Issuance      | InterestShortfall      |                  |
| Issuance      | RealisedLoss           |                  |

| Issuance | Purpose               |  |
|----------|-----------------------|--|
| Issuance | IssueSize             |  |
| Issuance | IssueNominalAmount    |  |
| Issuance | EventInformation      |  |
| Issuance | IssuedAsset           |  |
| Issuance | OriginalIssueDiscount |  |
| Issuance | IssuePlace            |  |
| Issuance | GlobalNoteType        |  |
| Issuance | CapitalRaised         |  |
| Issuance |                       |  |

| Issuance      | Minimum                         |         |
|---------------|---------------------------------|---------|
| Issuance      | IssuePrice                      |         |
| IssuerMeeting |                                 | Meeting |
| IssuerMeeting | IssuerMeetingIdentification     |         |
| IssuerMeeting | NomineePowerOfAttorneyIndicator |         |
| IssuerMeeting | NomineeVotingIndicator          |         |
| IssuerMeeting | NomineeBeneficialOwnerIndicator |         |
| IssuerMeeting | ProxyVotingIndicator            |         |
|               |                                 |         |

| IssuerMeeting | ProxyBeneficialOwnerIndicator |                            |
|---------------|-------------------------------|----------------------------|
| IssuerMeeting | ProxyPowerOfAttorneyIndicator |                            |
| IssuerMeeting | ValidCreditorIndicator        |                            |
| IssuerMeeting | CapitalStock                  |                            |
| IssuerRole    |                               | AssetPartyRole             |
| JointOwner    |                               | InvestmentAccountPartyRole |
| Jurisdiction  |                               |                            |
| Jurisdiction  | GovernanceRules               |                            |
| Jurisdiction  | Identification                |                            |
|               |                               |                            |

| Jurisdiction         | RegisteredSecurities  |                     |
|----------------------|-----------------------|---------------------|
| Jurisdiction         | AssociatedStrategy    |                     |
| Jurisdiction         | SecuritiesRestriction |                     |
| Jurisdiction         | RelatedSecuritiesTax  |                     |
| Jurisdiction         | RelatedMarket         |                     |
| Jurisdiction         | RelatedAgreement      |                     |
| JurisdictionStrategy |                       | PortfolioStrategy   |
| JurisdictionStrategy | Jurisdiction          |                     |
| LeadUnderwriter      |                       | SecuritiesPartyRole |
| Leg                  |                       |                     |
| Leg                  | RelatedAsset          |                     |

| Leg               | RatioQuantity |                            |
|-------------------|---------------|----------------------------|
| Leg               | Currency      |                            |
| Leg               | SwapType      |                            |
| Leg               | Pool          |                            |
| Leg               | Trade         |                            |
| LegalAdvisor      |               | SecuritiesPartyRole        |
| LegalGuardianRole |               | InvestmentAccountPartyRole |

| LegalRepresentative |                           | Role           |
|---------------------|---------------------------|----------------|
| Lender              |                           | TradePartyRole |
| LetterOfCredit      |                           | Asset          |
| LetterOfCredit      | Amount                    |                |
| LetterOfCredit      | Document                  |                |
| LetterOfCredit      | CommercialTradeSettlement |                |
| LifeCalculation     |                           |                |

| LifeCalculation | SecuritiesPricing    |  |
|-----------------|----------------------|--|
| LifeCalculation | VariableInterest     |  |
| LifeCalculation | Years                |  |
| LifeCalculation | CalculationType      |  |
| LifeCalculation | ValueDate            |  |
| LifeCalculation | ValuePeriod          |  |
| Limit           |                      |  |
| Limit           | Type                 |  |
| Limit           | Amount               |  |
| Limit           | CreditDebitIndicator |  |
| Limit           | UsedAmount           |  |
| Limit           | UsedPercentage       |  |

| Limit       | Currency                   |        |
|-------------|----------------------------|--------|
| Limit       | LimitStatus                |        |
| Limit       | Percentage                 |        |
| Limit       | RelatedDebitCreditFacility |        |
| Limit       | Periodicity                |        |
| Limit       | Quantity                   |        |
| Limit       | ValidityPeriod             |        |
| Limit       | RelatedPaymentCard         |        |
| Limit       | AvailableAmount            |        |
| LimitStatus |                            | Status |
| LimitStatus | Limit                      |        |
| LimitStatus | Status                     |        |

| LineItem |                                     |  |
|----------|-------------------------------------|--|
| LineItem | FinancialAdjustment                 |  |
| LineItem | LogisticsCharge                     |  |
| LineItem | GrossAmount                         |  |
| LineItem | Identification                      |  |
| LineItem | InvoicedProduct                     |  |
| LineItem | NetWeight                           |  |
| LineItem | BilledQuantity                      |  |
| LineItem | ChargeFreeQuantity                  |  |
| LineItem | MeasureQuantityStartRelatedLineItem |  |
| LineItem | MeasureQuantityEndRelatedLineItem   |  |

| LineItem | MeasureDateTimeStart |  |
|----------|----------------------|--|
| LineItem | MeasureDateTimeEnd   |  |
| LineItem | Invoice              |  |
| LineItem | NetAmount            |  |
| LineItem | Packaging            |  |
| LineItem | DeliveryDateTime     |  |
| LineItem | Charges              |  |
| LineItem | NetPriceCharge       |  |
| LineItem | GrossPriceQuantity   |  |
| LineItem | NetPriceQuantity     |  |
|          |                      |  |

| LineItem<br>GrossWeight               |
|---------------------------------------|
|                                       |
| Liquidity                             |
| Liquidity<br>Quantity                 |
| Liquidity<br>ListTrading              |
| Liquidity<br>IndicatorType            |
| Liquidity<br>Upper                    |
| Liquidity<br>Lower                    |
| Liquidity<br>Value                    |
| Liquidity<br>WeightedAverageLiquidity |

| LiquidityManagementLimit |                     | Limit |
|--------------------------|---------------------|-------|
| LiquidityManagementLimit | VolatilityMargin    |       |
| LiquidityManagementLimit | CurrencyExchange    |       |
| LiquidityManagementLimit | RelatedCashServices |       |
| LiquidityManagementLimit | LiquidityLimitType  |       |
| LiquidityManagementLimit | RequiredAmount      |       |

| ListTrading |                     |  |
|-------------|---------------------|--|
| ListTrading | ListIdentification  |  |
| ListTrading | SecuritiesListOrder |  |
| ListTrading | ListTradingSession  |  |
| ListTrading | ListName            |  |
| ListTrading | BasisPriceType      |  |
| ListTrading | StrikeTime          |  |
|             |                     |  |

| ListTrading<br>SellSideIdentification<br>ListTrading<br>BuySideIdentification<br>ListTrading<br>Liquidity<br>ListTrading<br>BidType<br>Loan<br>Debt<br>Loan<br>PrincipalAmount<br>Loan<br>InterestPaymentsSchedule | ListTrading | GrossAmountIndicator |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|----------------------|--|
|                                                                                                                                                                                                                    |             |                      |  |
|                                                                                                                                                                                                                    |             |                      |  |
|                                                                                                                                                                                                                    |             |                      |  |
|                                                                                                                                                                                                                    |             |                      |  |
|                                                                                                                                                                                                                    |             |                      |  |
|                                                                                                                                                                                                                    |             |                      |  |
|                                                                                                                                                                                                                    |             |                      |  |

| Loan                     | IntraCompanyLoanIndicator |                               |
|--------------------------|---------------------------|-------------------------------|
| LocalBroker              |                           | Broker                        |
| LocalDepositoryRole      |                           | DepositoryRole                |
| LocalName                |                           |                               |
| LocalName                | FullName                  |                               |
| LocalName                | RelatedSecurity           |                               |
| LocalName                | ShortName                 |                               |
| LocalName                | Language                  |                               |
| LocalSettlementAgentRole |                           | SecuritiesSettlementPartyRole |
| Location                 |                           |                               |
| Location                 | NativePerson              |                               |

| Location | System                         | System for which a location is<br>System<br>specified.                                                                                                                                               |
|----------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Location | DomiciledParty                 | Party which is domiciled in a<br>Party<br>specific location.                                                                                                                                         |
| Location | OperatingOrganisation          | Organisation which has its<br>Organisation<br>operations in a specific location.                                                                                                                     |
| Location | Address                        | Information that locates and<br>PostalAddress<br>identifies a specific address.                                                                                                                      |
| Location | IssuedDocument                 | Document which was issued at a<br>Document<br>specific location.                                                                                                                                     |
| Location | Incoterms                      | Incoterms associated with a<br>Incoterms<br>location.                                                                                                                                                |
| Location | DepartureTransportParameters   | Transport parameters linked to a<br>Transport<br>place of departure.                                                                                                                                 |
| Location | DestinationTransportParameters | Transport parameters linked to a<br>Transport<br>place of destination.                                                                                                                               |
| Location | InsuranceCertificate           | Insurance for which the claims<br>InsuranceCertificate<br>are payable at a specific location.                                                                                                        |
| Location | Party                          | Party which resides in a specific<br>Party<br>location.                                                                                                                                              |
| Location | RelatedExpiry                  | Expiry information which<br>Expiry<br>contains an expiry location.                                                                                                                                   |
| Location | RelatedJurisdiction            | Jurisdiction of the location.<br>Jurisdiction                                                                                                                                                        |
| Location | Identification                 | Identifies the location, for<br>instance, the name of an airport,<br>a county, a state, a province or a<br>GenericIdentification<br>city by a code or a text. eg LHR<br>for London Heathrow airport. |
|          |                                |                                                                                                                                                                                                      |

| Location     | TaxableParty           |  |
|--------------|------------------------|--|
| Location     | RegisteredOrganisation |  |
| Location     | RelatedTransport       |  |
| Location     | TimeZone               |  |
|              |                        |  |
| LotBreakdown |                        |  |
| LotBreakdown | LotUnit                |  |
| LotBreakdown | SecuritiesQuantity     |  |
| LotBreakdown | LotNumber              |  |
| LotBreakdown | LotDateTime            |  |
| LotBreakdown | LotPrice               |  |
| LotBreakdown | LotIdentifier          |  |
| LotBreakdown | TradeLotMarket         |  |
|              |                        |  |

| LotBreakdown          | QuoteLotMarket               |                  |
|-----------------------|------------------------------|------------------|
| LotBreakdown          | RoundLotMarket               |                  |
| Lottery               |                              |                  |
| Lottery               | LotteryDate                  |                  |
| Lottery               | IncrementalDenomination      |                  |
| Lottery               | LotteryType                  |                  |
| Lottery               | RelatedCorporateEvent        |                  |
| MailingInstructions   |                              |                  |
| MailingInstructions   | MailingIndicator             |                  |
| MailingInstructions   | RegistrationAddressIndicator |                  |
| MailingInstructions   | RelatedPostalAddress         |                  |
| ManagedAccountProduct |                              | FinancialProduct |
|                       |                              |                  |

| ManagedAccountProduct | Account                   |          |
|-----------------------|---------------------------|----------|
| ManagedAccountProduct | InvestmentAccountContract |          |
| Mandate               |                           | Contract |
| Mandate               | SignatureConditions       |          |
| Mandate               | MandateIdentification     |          |
| Mandate               | OriginalMandate           |          |
| Mandate               | Amendment                 |          |
| Mandate               | MandatePartyRole          |          |
| Mandate               | MandateStatus             |          |
| Mandate               | AccountContract           |          |
| Mandate               | Authentication            |          |
| Mandate               | TrackingDays              |          |

| Mandate          | TrackingIndicator  |                  |
|------------------|--------------------|------------------|
| Mandate          | Rate               |                  |
| Mandate          | Frequency          |                  |
| Mandate          | MandatePaymentType |                  |
| MandateHolder    |                    | MandatePartyRole |
| MandateIssuer    |                    | MandatePartyRole |
| MandatePartyRole |                    | Role             |
| MandatePartyRole | Mandate            |                  |
| MandateStatus    |                    | Status           |
| MandateStatus    | Accepted           |                  |
| MandateStatus    | RejectReason       |                  |
|                  |                    |                  |

| MandateStatus            | Mandate                                     |                      |
|--------------------------|---------------------------------------------|----------------------|
| MandateStatus            | MandateReason                               |                      |
| MandatoryCorporateAction |                                             | CorporateActionEvent |
| Manufacturer             |                                             | GoodsPartyRole       |
| MarginAmountRequirement  |                                             |                      |
| MarginAmountRequirement  | VariationMarginAmountRequirementCalculation |                      |
| MarginAmountRequirement  | DeliverMarginAmount                         |                      |
| MarginAmountRequirement  | ReturnMarginAmount                          |                      |
| MarginAmountRequirement  | SegregatedAmountRequirementCalculation      |                      |
|                          |                                             |                      |

| MarginAmountRequirement | IntraDayMarginCall           |  |
|-------------------------|------------------------------|--|
| MarginAmountRequirement | PeakInitialMarginLiability   |  |
| MarginAmountRequirement | AggregatePeakLiability       |  |
| MarginAmountRequirement | PeakVariationMarginLiability |  |
| MarginCall              |                              |  |
| MarginCall              | MarginCallValuationDate      |  |
| MarginCall              | AgreedAmount                 |  |
| MarginCall              | VariationMargin              |  |
|                         |                              |  |

| MarginCall | SegregatedIndependentAmount             |  |
|------------|-----------------------------------------|--|
| MarginCall | DefaultFundContribution                 |  |
| MarginCall | ExpectedVariationMarginType             |  |
| MarginCall | ExpectedSegregatedIndependentAmountType |  |
| MarginCall | TotalMarkToMarket                       |  |
| MarginCall | MarkToMarketNetted                      |  |
| MarginCall | MarkToMarketGross                       |  |
| MarginCall | MarkToMarketFails                       |  |
| MarginCall | FailsHaircut                            |  |
|            |                                         |  |

| MarginCall | InitialMargin                        |  |
|------------|--------------------------------------|--|
| MarginCall | IncreaseCoverage                     |  |
| MarginCall | CollateralisedMarginAccountIndicator |  |
| MarginCall | CollateralMovement                   |  |
| MarginCall | RelatedManagementProcess             |  |
| MarginCall | Security                             |  |
| MarginCall | MarginProduct                        |  |
| MarginCall | MarginType                           |  |
|            |                                      |  |

| MarginCall  | TotalMarginAmount       |  |
|-------------|-------------------------|--|
| Market      |                         |  |
| Market      | Trade                   |  |
| Market      | Jurisdiction            |  |
| Market      | Country                 |  |
| Market      | GeographicalEnvironment |  |
| Market      | Identification          |  |
| MarketClaim |                         |  |
| MarketClaim | MarketClaimAmount       |  |

| MarketClaim             | MarketClaimTrackingEndDate |                          |
|-------------------------|----------------------------|--------------------------|
| MarketClaim             | RelatedCorporateEvent      |                          |
| MarketClaimCounterparty |                            | CorporateActionPartyRole |
| MarketInfrastructure    |                            | Role                     |
| MarketInfrastructure    | AccountLink                |                          |
| MasterAgreement         |                            | Agreement                |
| MasterAgreement         | CollateralAgreement        |                          |
| MasterAgreement         | MasterAgreementType        |                          |

| MasterAgreement | GovernedTrades   |        |
|-----------------|------------------|--------|
| MasterAgreement | GovernedContract |        |
| MasterAgreement | GoverningLaw     |        |
| MatchingSystem  |                  | System |
| Meeting         |                  |        |
| Meeting         | DateAndTime      |        |
| Meeting         | DateStatus       |        |
| Meeting         | MeetingLocation  |        |
| Meeting         | Identification   |        |
| Meeting         | Deadline         |        |
|                 |                  |        |

| Meeting | MeetingServicing       |  |
|---------|------------------------|--|
| Meeting | Person                 |  |
| Meeting | PartyRole              |  |
| Meeting | Status                 |  |
| Meeting | CorporateEvent         |  |
| Meeting | Quorum                 |  |
| Meeting | VotingCondition        |  |
| Meeting | AttendanceRequired     |  |
| Meeting | AttendanceConfirmation |  |
| Meeting | IncentivePremium       |  |
| Meeting | Participation          |  |

| Meeting           | ResolutionProposalConditions  |  |
|-------------------|-------------------------------|--|
| Meeting           | AgendaItem                    |  |
| Meeting           | ProxyAppointmentConditions    |  |
| Meeting           | AdditionalRight               |  |
| Meeting           | Type                          |  |
| Meeting           | PowerOfAttorneyRequirements   |  |
| Meeting           | MeetingEventClassification    |  |
| Meeting           | AttendanceAdmissionConditions |  |
| MeetingAttendance |                               |  |
| MeetingAttendance | AttendanceCard                |  |

| MeetingAttendance   | PercentageOfVotingRights |                  |
|---------------------|--------------------------|------------------|
| MeetingAttendance   | RelatedMeeting           |                  |
| MeetingAttendeeRole |                          | MeetingPartyRole |
| MeetingAttendeeRole | Person                   |                  |
| MeetingDeadline     |                          | Deadline         |
| MeetingEntitlement  |                          |                  |
| MeetingEntitlement  | EntitlementFixingDate    |                  |
| MeetingEntitlement  | EntitlementRatio         |                  |
| MeetingEntitlement  | EligiblePosition         |                  |
|                     |                          |                  |

| MeetingEntitlement   | RelatedServicing                  |                  |
|----------------------|-----------------------------------|------------------|
| MeetingEntitlement   | EntitlementCalculationDate        |                  |
| MeetingInitiatorRole |                                   | MeetingPartyRole |
| MeetingNotice        |                                   |                  |
| MeetingNotice        | RelatedServicing                  |                  |
| MeetingNotice        | BeneficialOwnerExclusiveIndicator |                  |
| MeetingNotice        | ParticipationMethod               |                  |
| MeetingParticipation |                                   |                  |

| MeetingParticipation<br>TotalNumberOfVotingRights<br>MeetingParticipation<br>CalculationDate<br>MeetingParticipation<br>TotalNumberOfSecurities<br>MeetingParticipation<br>Meeting<br>MeetingParticipationRegistrationDeadline<br>MeetingDeadline |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| MeetingPartyRole<br>CorporateActionPartyRole                                                                                                                                                                                                      |
| MeetingPartyRole<br>Meeting                                                                                                                                                                                                                       |
| MeetingResultDissemination                                                                                                                                                                                                                        |
| MeetingResultDissemination<br>RelatedServicing                                                                                                                                                                                                    |

| MeetingResultDissemination | VoteResult                 |                          |
|----------------------------|----------------------------|--------------------------|
| MeetingServicing           |                            | CorporateActionServicing |
| MeetingServicing           | MeetingSpecification       |                          |
| MeetingServicing           | MeetingNotice              |                          |
| MeetingServicing           | MeetingEntitlement         |                          |
| MeetingServicing           | MeetingInstruction         |                          |
| MeetingServicing           | MeetingResultDissemination |                          |
| MeetingStatus              |                            | Status                   |
| MeetingStatus              | MeetingResolutionStatus    |                          |
|                            |                            |                          |

| MeetingStatus       | InstructionCancellationStatus |                      |
|---------------------|-------------------------------|----------------------|
| MeetingStatus       | Reason                        |                      |
| MeetingStatus       | NotificationStatus            |                      |
| MeetingStatus       | Meeting                       |                      |
| MeetingStatusReason |                               | StatusReason         |
| MeetingStatusReason | MeetingCancellationReason     |                      |
| MeetingStatusReason | MeetingStatus                 |                      |
| MeetingStatusReason | InstructionRejectionReason    |                      |
| MerchantRole        |                               | CardPaymentPartyRole |
| MerchantRole        | MerchantCategoryCode          |                      |
| MerchantRole        | MerchantIdentification        |                      |

| ModelForm   |                          |       |
|-------------|--------------------------|-------|
| ModelForm   | GovernanceRules          |       |
| ModelForm   | Undertaking              |       |
| ModelForm   | Identification           |       |
| ModelForm   | Version                  |       |
| ModelForm   | RequestedWordingLanguage |       |
| ModelForm   | EffectiveDate            |       |
| Money       |                          | Asset |
|             |                          |       |
| Money       | CashAmount               |       |
| Negotiation |                          |       |
| Negotiation | TradingMethod            |       |
| Negotiation | TradeExecution           |       |

| Negotiation              | TradingSystem             |  |
|--------------------------|---------------------------|--|
| Negotiation              | NegotiationIdentification |  |
| Negotiation              | Quote                     |  |
| Negotiation              | IndicationOfInterest      |  |
| Negotiation              | SecuritiesOrder           |  |
| NetAssetValueCalculation |                           |  |
| NetAssetValueCalculation | ValuationFrequency        |  |
| NetAssetValueCalculation | ValuationDateTime         |  |
| NetAssetValueCalculation | NetAssetValue             |  |
| NetAssetValueCalculation | RelatedFund               |  |
| NetAssetValueCalculation | ValuationType             |  |
| NetAssetValueCalculation | SuspendedIndicator        |  |
|                          |                           |  |

| NetAssetValueCalculation | ForExecutionIndicator            |
|--------------------------|----------------------------------|
| NetAssetValueCalculation | TaxLiability                     |
| NetAssetValueCalculation | TaxRefund                        |
| NetAssetValueCalculation | OfficialValuationIndicator       |
| NetAssetValueCalculation | EstimatedPriceIndicator          |
| NetAssetValueCalculation | ValuationStatistics              |
| NetAssetValueCalculation | InvestmentFundPerformanceFactors |
| NetAssetValueCalculation | Price                            |
| NetAssetValueCalculation | SecuritiesQuantity               |
| NetAssetValueCalculation | Interest                         |
| NetAssetValueCalculation | FundsCashFlow                    |

| NetAssetValueCalculation | DeclarationChannel               |                      |
|--------------------------|----------------------------------|----------------------|
| NetAssetValueCalculation | DeclarationDate                  |                      |
| NetAssetValueCalculation | FirstValuationDate               |                      |
| NetAssetValueCalculation | HistoricPricingIndicator         |                      |
| Netting                  |                                  | ObligationFulfilment |
| Netting                  | AverageDealPrice                 |                      |
| Netting                  | RelatedSecuritiesClearingProcess |                      |
| Netting                  | NetPositionAmount                |                      |
| Netting                  | AmountDirection                  |                      |
| Netting                  | NetQuantity                      |                      |
| Netting                  | PositionAmount                   |                      |
| NetworkAccess            |                                  |                      |
| NetworkAccess            | HostIPAddress                    |                      |
| NetworkAccess            | HostPortNumber                   |                      |
|                          |                                  |                      |

| NetworkAccess         | UserName                 |                            |
|-----------------------|--------------------------|----------------------------|
| NetworkAccess         | AccessCode               |                            |
| NetworkAccess         | ClientCertificate        |                            |
| NetworkAccess         | TerminalManagementSystem |                            |
| NetworkAccess         | NetworkAddress           |                            |
| Nominee               |                          | InvestmentAccountPartyRole |
| NonClearingMemberRole |                          | ThirdPartyRole             |
| NonDeliverableTrade   |                          | ForeignExchangeTrade       |
| NonDeliverableTrade   | SettlementCurrency       |                            |
| NonDeliverableTrade   | FixingConditions         |                            |
|                       |                          |                            |

| NonDeliverableTrade     | OpeningLeg      |             |
|-------------------------|-----------------|-------------|
| NonDeliverableTrade     | ClosingLeg      |             |
| NonDisclosedListTrading |                 | ListTrading |
| NonDisclosedListTrading | BidByCurrency   |             |
| NonDisclosedListTrading | BidBySector     |             |
| NonDisclosedListTrading | BidByIndex      |             |
| NonDisclosedListTrading | NumberOfBidders |             |
|                         |                 |             |

| NonDisclosedListTrading | SideValue          |                          |
|-------------------------|--------------------|--------------------------|
| NonExecutingBroker      |                    | SecuritiesOrderPartyRole |
| NonFinancialInstitution |                    | Organisation             |
| NotificationReceiver    |                    | DocumentPartyRole        |
| NotifyingParty          |                    | DocumentPartyRole        |
| Novation                |                    | ObligationFulfilment     |
| Novation                | SecuritiesClearing |                          |
| Novation                | NovationStatus     |                          |
| Obligation              |                    |                          |

| Obligation<br>RequestedSettlementDate   |  |
|-----------------------------------------|--|
| Obligation<br>RequestedSettlementAmount |  |
| Obligation<br>Priority                  |  |
| Obligation<br>Trade                     |  |
| Obligation<br>TransactionRisk           |  |
| Obligation<br>ParentObligation          |  |
| Obligation<br>SubObligation             |  |

| Obligation           | Offset                    |  |
|----------------------|---------------------------|--|
| Obligation           | OriginalObligationProcess |  |
| Obligation           | ExposureType              |  |
| Obligation           | TreasuryTrade             |  |
| ObligationFulfilment |                           |  |
| ObligationFulfilment | Date                      |  |
| ObligationFulfilment | ObligationOffset          |  |
| ObligationFulfilment | ResultingObligation       |  |

| ObligorBank        |                             | CommercialTradePartyRole |
|--------------------|-----------------------------|--------------------------|
| OperationThreshold |                             |                          |
| OperationThreshold | BankOperation               |                          |
| OperationThreshold | MininumAmountPerTransaction |                          |
| OperationThreshold | MaximumAmount               |                          |
| Option             |                             | Derivative               |
| Option             | InstrumentAssignmentMethod  |                          |
| Option             | SettleStyle                 |                          |
| Option             | Standardisation             |                          |

| Option | PositionLimit               |  |
|--------|-----------------------------|--|
| Option | UnderlyingType              |  |
| Option | CoverIndicator              |  |
| Option | OptionConversionInformation |  |
| Option | OptionRatio                 |  |
| Option | SecuritiesOptionTrade       |  |
| Option | SettlementType              |  |
| Option | StrikeMultiplier            |  |
| Option | ExpiryLocation              |  |
|        |                             |  |

| Option | FinalSettlementDate  |  |
|--------|----------------------|--|
| Option | OptionStyle          |  |
| Option | CurrencyOption       |  |
| Option | EarliestExerciseDate |  |
| Option | SettlementDays       |  |
| Option | StrikePrice          |  |
| Option | OptionStartDate      |  |
| Option | ExpiryDateAndTime    |  |
| Option | OptionType           |  |

| Option                 | StrikeValue          |                          |
|------------------------|----------------------|--------------------------|
| Option                 | SettlementPeriodType |                          |
| Order                  |                      |                          |
| Order                  | Trade                |                          |
| Order                  | MasterIdentification |                          |
| OrderBook              |                      |                          |
| OrderBook              | Order                |                          |
| OrderBook              | PriceTimePriority    |                          |
| OrderOriginationFirm   |                      | SecuritiesOrderPartyRole |
| OrderOriginationTrader |                      | SecuritiesOrderPartyRole |
|                        |                      |                          |

| Organisation |                            | Party |
|--------------|----------------------------|-------|
| Organisation | Purpose                    |       |
| Organisation | RegistrationDate           |       |
| Organisation | OrganisationIdentification |       |
| Organisation | ParentOrganisation         |       |
| Organisation | Branch                     |       |
| Organisation | SecuritiesModification     |       |
| Organisation | PlaceOfOperation           |       |
| Organisation | PlaceOfRegistration        |       |
| Organisation | Description                |       |
| Organisation | LegalStructure             |       |

| Organisation<br>Sector<br>Organisation<br>RelatedIndicationOfInterest<br>Organisation<br>Strategy<br>Organisation<br>OrganisationHierarchy<br>Organisation<br>RepresentativeOfficer<br>Organisation<br>EstablishmentDate<br>Organisation<br>EntityExpirationDate<br>Organisation<br>EntityExpirationReason<br>Organisation<br>EntityStatus<br>Organisation<br>MerchantCategory |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                |  |  |

| Organisation               | Logo                                     |                                |
|----------------------------|------------------------------------------|--------------------------------|
| Organisation               | RelatedUltimateCreditrorEnrolmentService |                                |
| Organisation               | RelatedCreditrorEnrolmentService         |                                |
| Organisation               | RelatedPostTradeRiskReduction            |                                |
| OrganisationHierarchy      |                                          |                                |
| OrganisationHierarchy      | Organisation                             |                                |
| OrganisationIdentification |                                          | PartyIdentificationInformation |
| OrganisationIdentification | BICFI                                    |                                |
| OrganisationIdentification | AnyBIC                                   |                                |

| OrganisationIdentification | OrganisationName                       |
|----------------------------|----------------------------------------|
| OrganisationIdentification | Organisation                           |
| OrganisationIdentification | ClearingSystemMemberIdentificationType |
| OrganisationIdentification | BICNonFI                               |
| OrganisationIdentification | EANGLN                                 |

| OrganisationIdentification | CHIPSUniversalIdentifier |  |
|----------------------------|--------------------------|--|
| OrganisationIdentification | DUNS                     |  |
| OrganisationIdentification | BankPartyIdentification  |  |
| OrganisationIdentification | MIC                      |  |
| OrganisationIdentification | LEI                      |  |
| OrganisationIdentification | ELF                      |  |

| OrganisationIdentification | AdditionalLEIAttributes |                      |
|----------------------------|-------------------------|----------------------|
| OrganisationName           |                         | PartyName            |
| OrganisationName           | Organisation            |                      |
| OrganisationName           | LegalName               |                      |
| OrganisationName           | TradingName             |                      |
| OrganisationName           | ShortName               |                      |
| OrganisationStrategy       |                         | PortfolioStrategy    |
| OrganisationStrategy       | Organisation            |                      |
| POIManufacturer            |                         | CardPaymentPartyRole |
| Packaging                  |                         |                      |
| Packaging                  | Quantity                |                      |
| Packaging                  | PerPackageUnitQuantity  |                      |

| Packaging | Transport                   |                      |
|-----------|-----------------------------|----------------------|
| Packaging | PackagingName               |                      |
| Packaging | TotalConsignmentQuantity    |                      |
| Packaging | TotalVolume                 |                      |
| Packaging | TotalWeight                 |                      |
| Packaging | RelatedLineItem             |                      |
| Packaging | PackageType                 |                      |
| PairOff   |                             | ObligationFulfilment |
| PairOff   | PairedOffQuantity           |                      |
| PairOff   | RelatedSecuritiesSettlement |                      |
| Party     |                             | RolePlayer           |
| Party     | ContactPoint                |                      |

| Party | Identification       |
|-------|----------------------|
| Party | MoneyLaunderingCheck |
| Party | TaxationConditions   |
| Party | Domicile             |
| Party | Residence            |
| Party | PowerOfAttorney      |
| Party | Location             |
| Party | CloseLinkSecurity    |
| Party | CreditQuality        |
| Party | ShareholdingType     |

| Party                          | RelatedCareOf              |  |
|--------------------------------|----------------------------|--|
| PartyIdentificationInformation |                            |  |
| PartyIdentificationInformation | OtherIdentification        |  |
| PartyIdentificationInformation | IdentifiedParty            |  |
| PartyIdentificationInformation | TaxIdentificationNumber    |  |
| PartyIdentificationInformation | NationalRegistrationNumber |  |
| PartyIdentificationInformation | TypeOfIdentification       |  |
| PartyIdentificationInformation | Declaration                |  |
| PartyIdentificationInformation | PartyType                  |  |
| PartyIdentificationInformation | PartyName                  |  |
|                                |                            |  |

| PartyIdentificationInformation | ValidityPeriod                      |                 |
|--------------------------------|-------------------------------------|-----------------|
| PartyIdentificationInformation | IdentifiedMarket                    |                 |
| PartyIdentificationInformation | RelatedApprovedBenchmark            |                 |
| PartyIdentificationInformation | RelatedAdministratedBenchmark       |                 |
| PartyIdentificationInformation | RegistrationAuthorityIdentification |                 |
| PartyName                      |                                     |                 |
| PartyName                      | Name                                |                 |
| PartyName                      | PartyIdentification                 |                 |
| Payee                          |                                     | ChequePartyRole |
| PayingAgentRole                |                                     |                 |
|                                |                                     |                 |

| PayingAgentRole | CommissionAmount   |                      |
|-----------------|--------------------|----------------------|
| Payment         |                    | ObligationFulfilment |
| Payment         | PaymentObligation  |                      |
| Payment         | CurrencyOfTransfer |                      |
| Payment         | CreditMethod       |                      |
| Payment         | Type               |                      |
| Payment         | InstructedAmount   |                      |
| Payment         | Priority           |                      |
| Payment         | ValueDate          |                      |
| Payment         | PaymentStatus      |                      |

| Payment | PartyRole                   |
|---------|-----------------------------|
| Payment | TaxOnPayment                |
| Payment | PaymentExecution            |
| Payment | PoolingAdjustmentDate       |
| Payment | EquivalentAmount            |
| Payment | CurrencyExchange            |
| Payment | InstructionForCreditorAgent |

| Payment     | ReturnPayment               |  |
|-------------|-----------------------------|--|
| Payment     | RelatedSecuritiesSettlement |  |
| Payment     | InvoiceReconciliation       |  |
| Payment     | PaymentInstrument           |  |
| Payment     | Account                     |  |
| Payment     | Adjustments                 |  |
| Payment     | ContractRegistration        |  |
| PaymentCard |                             |  |
| PaymentCard | Payment                     |  |
| PaymentCard | Type                        |  |
| PaymentCard | Number                      |  |

| PaymentCard | StartDate              |  |
|-------------|------------------------|--|
| PaymentCard | ExpiryDate             |  |
| PaymentCard | SecurityCode           |  |
| PaymentCard | SequenceNumber         |  |
| PaymentCard | ServiceCode            |  |
| PaymentCard | TrackValue             |  |
| PaymentCard | SecurityCodeManagement |  |
| PaymentCard | CardBrand              |  |
| PaymentCard | RelatedAccount         |  |
| PaymentCard | ProfileNumber          |  |
| PaymentCard | RelatedAccountType     |  |
| PaymentCard | CreditAvailableAmount  |  |
| PaymentCard | Limit                  |  |
| PaymentCard | CardCurrencyCode       |  |
|             |                        |  |

| PaymentCard      | Interest               |  |
|------------------|------------------------|--|
| PaymentCard      | CardCountryCode        |  |
| PaymentCard      | CardProgramme          |  |
| PaymentExecution |                        |  |
| PaymentExecution | CreditDebitIndicator   |  |
| PaymentExecution | CreationDate           |  |
| PaymentExecution | AcceptanceDateTime     |  |
| PaymentExecution | Payment                |  |
| PaymentExecution | ProcessingInstructions |  |
|                  |                        |  |

| PaymentExecution      | RequestedExecutionDate             |                     |
|-----------------------|------------------------------------|---------------------|
| PaymentExecution      | RelatedInvestigationCase           |                     |
| PaymentExecution      | RelatedInvestigationCaseResolution |                     |
| PaymentExecution      | Next                               |                     |
| PaymentExecution      | CurrencyExchange                   |                     |
| PaymentExecution      | ExpiryDateTime                     |                     |
| PaymentIdentification |                                    | TradeIdentification |
| PaymentIdentification | ExecutionIdentification            |                     |
|                       |                                    |                     |

| PaymentIdentification | EndToEndIdentification    |  |
|-----------------------|---------------------------|--|
| PaymentIdentification | InstructionIdentification |  |
| PaymentIdentification | TransactionIdentification |  |
| PaymentIdentification | ClearingSystemReference   |  |
| PaymentIdentification | CreditorReference         |  |
| PaymentIdentification | Payment                   |  |
| PaymentIdentification | UETR                      |  |

| PaymentInitiation  |                         | PaymentExecution |
|--------------------|-------------------------|------------------|
| PaymentInstruction |                         | PaymentExecution |
| PaymentInstruction | ProcessingValidityTime  |                  |
| PaymentInstruction | InstructionForNextAgent |                  |
| PaymentInstruction | SettlementInstruction   |                  |

| PaymentInstruction       | ClearingChargeAmount |                   |
|--------------------------|----------------------|-------------------|
| PaymentInstruction       | StandingOrder        |                   |
| PaymentInstruction       | Previous             |                   |
| PaymentInvestigationCase |                      | InvestigationCase |
| PaymentInvestigationCase | PaymentStatus        |                   |
| PaymentInvestigationCase | CancellationReason   |                   |
| PaymentInvestigationCase | UnderlyingPayment    |                   |
|                          |                      |                   |

| PaymentInvestigationCase          | MissingCoverIndication     |  |
|-----------------------------------|----------------------------|--|
| PaymentInvestigationCase          | UnderlyingInstruction      |  |
| PaymentInvestigationCase          | UnderlyingCashEntry        |  |
| PaymentInvestigationCase          | IncorrectInformationReason |  |
| PaymentInvestigationCase          | MissingInformationReason   |  |
| PaymentInvestigationCase          | CaseType                   |  |
| PaymentInvestigationCaseRejection |                            |  |
| PaymentInvestigationCaseRejection | RejectedModification       |  |
| PaymentInvestigationCaseRejection | RejectedCancellation       |  |
| PaymentInvestigationCaseRejection | RejectedCancellationReason |  |

| If yes, it means the cancellation<br>of the assignment is confirmed.If<br>no, it means the cancellation of<br>PaymentInvestigationCaseRejection<br>AssignmentCancellationConfirmation<br>the assignment is rejected and<br>the investigation process will<br>continue. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PaymentInvestigationCaseRejection<br>RejectionReason                                                                                                                                                                                                                   |
| PaymentInvestigationCaseRejection<br>RelatedInvestigationCaseResolution                                                                                                                                                                                                |
| PaymentInvestigationCaseRejection<br>InvestigationRejection                                                                                                                                                                                                            |
| PaymentInvestigationCaseResolution<br>InvestigationResolution                                                                                                                                                                                                          |
| PaymentInvestigationCaseResolution<br>InvestigationStatus                                                                                                                                                                                                              |
| PaymentInvestigationCaseResolution<br>DebitAuthorisationConfirmation                                                                                                                                                                                                   |
| PaymentInvestigationCaseResolution<br>CoverCorrection                                                                                                                                                                                                                  |
| PaymentInvestigationCaseResolution<br>EntryCorrection                                                                                                                                                                                                                  |

| PaymentInvestigationCaseResolution<br>PaymentCorrection<br>PaymentInvestigationCaseResolution<br>PaymentExecutionCorrection<br>PaymentInvestigationCaseResolution<br>InvestigationCaseRejection<br>PaymentInvestigationCaseResolution<br>DuplicateCase<br>PaymentObligation<br>Obligation<br>PaymentObligation<br>PaymentOffset<br>PaymentObligation<br>Purpose<br>PaymentObligation<br>RemittanceDeliveryMethod |  |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |

| PaymentObligation | AssociatedDocument |  |
|-------------------|--------------------|--|
| PaymentObligation | Amount             |  |
| PaymentObligation | RemittanceLocation |  |
| PaymentObligation | Interest           |  |
| PaymentObligation | CommercialTrade    |  |
| PaymentObligation | Percentage         |  |
| PaymentObligation | MaximumAmount      |  |
| PaymentObligation | ExpiryDate         |  |
| PaymentObligation | ApplicableLaw      |  |
| PaymentObligation | PaymentSourceBuyIn |  |
|                   |                    |  |

| PaymentObligation<br>RelatedCorporateAction         |
|-----------------------------------------------------|
| PaymentObligation<br>RelatedCollateralMovement      |
| PaymentObligation<br>PaymentSourceUndertakingDemand |
| PaymentObligation<br>PartyRole                      |
| PaymentObligation<br>ExecutedSecuritiesTrade        |
| PaymentObligation<br>RelatedAccountClosingTerms     |
| PaymentObligation<br>PaymentSourcePortfolioTransfer |
| PaymentObligation<br>PaymentSourceCurrencyOption    |
| PaymentObligation<br>ExchangeRateInformation        |
| PaymentObligation<br>Dividend                       |

| PaymentObligation          | RepurchaseAgreement |      |
|----------------------------|---------------------|------|
| PaymentObligation          | RelatedAssignment   |      |
| PaymentObligation          | BankingTransaction  |      |
| PaymentObligation          | PaymentTerms        |      |
| PaymentObligation          | PaymentDueDate      |      |
| PaymentObligationPartyRole |                     | Role |
| PaymentObligationPartyRole | PaymentObligation   |      |
| PaymentPartyRole           |                     | Role |
| PaymentPartyRole           | CashAccount         |      |
| PaymentPartyRole           | Payment             |      |
| PaymentProcessing          |                     |      |

| PaymentProcessing<br>Priority         |
|---------------------------------------|
| PaymentProcessing<br>ServiceLevel     |
| PaymentProcessing<br>ClearingChannel  |
| PaymentProcessing<br>LocalInstrument  |
| PaymentProcessing<br>CategoryPurpose  |
| PaymentProcessing<br>PaymentExecution |
| PaymentProcessing<br>SequenceType     |
| PaymentProcessing<br>RelatedMandate   |
| PaymentProcessing<br>BankTransaction  |
| PaymentProcessing<br>ContactPoint     |

| PaymentProcessing | AdviceType                 |        |
|-------------------|----------------------------|--------|
| PaymentSchedule   |                            |        |
| PaymentSchedule   | Date                       |        |
| PaymentSchedule   | Amount                     |        |
| PaymentSchedule   | Rate                       |        |
| PaymentStatus     |                            | Status |
| PaymentStatus     | Status                     |        |
| PaymentStatus     | Payment                    |        |
| PaymentStatus     | UnmatchedStatusReason      |        |
| PaymentStatus     | SuspendedStatusReason      |        |
| PaymentStatus     | PendingSettlement          |        |
| PaymentStatus     | InstructionStatus          |        |
| PaymentStatus     | TransactionRejectionReason |        |
|                   |                            |        |

| PaymentStatus | RelatedInvestigationCase |  |
|---------------|--------------------------|--|
| PaymentStatus | NotificationStatus       |  |
| PaymentStatus | TransactionStatus        |  |
| PaymentStatus | CashPaymentStatus        |  |
| PaymentStatus | UnsuccessfulStatusReason |  |
| PaymentStatus | CancellationReason       |  |
| PaymentStatus | MandateRejectionReason   |  |
| PaymentStatus | PendingFailingSettlement |  |
| PaymentTerms  |                          |  |
| PaymentTerms  | Amount                   |  |
| PaymentTerms  | Percentage               |  |
| PaymentTerms  | PaymentPeriod            |  |
|               |                          |  |

| PaymentTerms   | RelatedPaymentObligation   |            |
|----------------|----------------------------|------------|
| PaymentTerms   | PaymentTime                |            |
| PaymentTerms   | RelatedPaymentScheduleType |            |
| PaymentTerms   | RelatedLoan                |            |
| PaymentTracker |                            |            |
| PaymentTracker | Agent                      |            |
| PaymentTracker | ChargesAmount              |            |
| PaymentTracker | ChargeBearer               |            |
| PaymentTracker | ExchangeRateData           |            |
| Penalty        |                            | Adjustment |
| Penalty        | PenaltyBasisAmount         |            |

| Pension |                       |  |
|---------|-----------------------|--|
| Pension | ValueOfPensionPolicy  |  |
| Pension | RelatedInvestmentPlan |  |
| Pension | EstimatedValue        |  |
| Pension | TransferScope         |  |
| Pension | Drawdown              |  |
| Pension | PensionOrderType      |  |
| Pension | RetirementAge         |  |
| Pension | Identification        |  |
| Pension | Type                  |  |
| Pension | TaxFreeCashAmount     |  |
| Pension | LumpSumType           |  |
| Pension | TaxReference          |  |

| Pension             | ClientLifetimeAllowanceProtection |       | Indicates whether the client has<br>any lifetime allowance protection.                                                                                                                             | YesNoIndicator |                    |
|---------------------|-----------------------------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|--------------------|
| PercentageAndPeriod |                                   |       | Relates a percentage to a period<br>of time.                                                                                                                                                       |                |                    |
| PercentageAndPeriod | Period                            |       | Period related to percentage.                                                                                                                                                                      | DateTimePeriod | Percentage         |
| PercentageAndPeriod | Percentage                        |       | Percentage rate.                                                                                                                                                                                   | PercentageRate |                    |
| PerformanceFactors  |                                   |       | Performance factors of the<br>investment fund / fund class.                                                                                                                                        |                |                    |
| PerformanceFactors  | NetAssetValueCalculation          |       | Calculation for which the<br>performance factors are<br>obtained.                                                                                                                                  |                |                    |
| PerformanceFactors  | CorporateActionFactor             |       | Value of the NAV before all<br>corporate events of the valuation<br>date, divided by the value of the<br>NAV after the corporate event.                                                            | DecimalNumber  |                    |
| PerformanceFactors  | CumulativeCorporateActionFactor   |       | Value of the NAV before a<br>corporate event, divided by the<br>value of the NAV after the<br>corporate event, accumulated for<br>a number of corporate events<br>over the defined period of time. | DecimalNumber  |                    |
| PerformanceFactors  | AccumulationPeriod                |       | Period of time for the calculation<br>of the cumulative corporate<br>action factor.                                                                                                                | DateTimePeriod | PerformanceFactors |
| PerformanceFactors  | NormalPerformance                 |       | Normal performance value of the<br>NAV.                                                                                                                                                            | DecimalNumber  |                    |
| Person              |                                   | Party | Human entity, as distinguished<br>from a corporate entity (which is<br>sometimes referred to as an<br>'artificial person').                                                                        |                |                    |

| Person | Gender                |  |
|--------|-----------------------|--|
| Person | Language              |  |
| Person | BirthDate             |  |
| Person | PlaceOfBirth          |  |
| Person | Profession            |  |
| Person | ResidentialStatus     |  |
| Person | Nationality           |  |
| Person | MinorIndicator        |  |
| Person | BusinessFunctionTitle |  |
| Person | PersonIdentification  |  |
| Person | EmployingParty        |  |

| Person               | MeetingAttendee        |                                |
|----------------------|------------------------|--------------------------------|
| Person               | RelatedRole            |                                |
| Person               | PreAssignedProxyPerson |                                |
| Person               | PersonProfile          |                                |
| Person               | ContactPersonRole      |                                |
| Person               | Household              |                                |
| Person               | CivilStatus            |                                |
| Person               | DeathDate              |                                |
| Person               | CitizenshipEndDate     |                                |
| Person               | CitizenshipStartDate   |                                |
| PersonIdentification |                        | PartyIdentificationInformation |
| PersonIdentification | SocialSecurityNumber   |                                |
| PersonIdentification | Person                 |                                |
|                      |                        |                                |

| PersonIdentification | PersonName                   |           |
|----------------------|------------------------------|-----------|
| PersonIdentification | DriversLicenseNumber         |           |
| PersonIdentification | AlienRegistrationNumber      |           |
| PersonIdentification | PassportNumber               |           |
| PersonIdentification | IdentityCardNumber           |           |
| PersonIdentification | EmployerIdentificationNumber |           |
| PersonName           |                              | PartyName |
| PersonName           | BirthName                    |           |
| PersonName           | NamePrefix                   |           |
| PersonName           | GivenName                    |           |
| PersonName           | MiddleName                   |           |

| PersonName    | NameSuffix                   |  |
|---------------|------------------------------|--|
| PersonName    | Identification               |  |
| PersonProfile |                              |  |
| PersonProfile | ForeignStatusCertification   |  |
| PersonProfile | EmployeeTerminationIndicator |  |
| PersonProfile | KnowYourCustomerCheckType    |  |
| PersonProfile | RiskLevel                    |  |
| PersonProfile | Person                       |  |

| PersonProfile | PoliticalExposureType           |              |
|---------------|---------------------------------|--------------|
| PersonProfile | CustomerConductClassification   |              |
| PersonProfile | FamilyMedicalInsuranceIndicator |              |
| PersonProfile | ProfileCertification            |              |
| PersonProfile | SourceOfWealth                  |              |
| PersonProfile | SalaryRange                     |              |
| PersonProfile | PoliticallyExposedStatus        |              |
| PhoneAddress  |                                 | ContactPoint |
| PhoneAddress  | PhoneNumber                     |              |
|               |                                 |              |

| PhoneAddress      | FaxNumber                  |                               |
|-------------------|----------------------------|-------------------------------|
| PhoneAddress      | MobileNumber               |                               |
| PhysicalDelivery  |                            |                               |
| PhysicalDelivery  | RelatedTransfer            |                               |
| PhysicalDelivery  | RegisteredAddressIndicator |                               |
| PhysicalDelivery  | IssuedCertificateNumber    |                               |
| PhysicalDelivery  | Address                    |                               |
| PhysicalDelivery  | Type                       |                               |
| PlaceOfRegistry   |                            | SecuritiesPartyRole           |
| PlaceOfSettlement |                            | SecuritiesSettlementPartyRole |

| PlaceOfSettlement  | SettlementMarket                   |                         |
|--------------------|------------------------------------|-------------------------|
| PlacementAgent     |                                    | InvestmentFundPartyRole |
| Pledgee            |                                    | SecuritiesPartyRole     |
| Pledgee            | PledgeeType                        |                         |
| Pledgee            | SecuritiesBalance                  |                         |
| PointOfInteraction |                                    | System                  |
| PointOfInteraction | CardPaymentAcquiring               |                         |
| PointOfInteraction | CardReadingCapabilities            |                         |
| PointOfInteraction | CardholderVerificationCapabilities |                         |

| PointOfInteraction | OnLineCapabilities                  |  |
|--------------------|-------------------------------------|--|
| PointOfInteraction | DisplayCapabilities                 |  |
| PointOfInteraction | PrintLineWidth                      |  |
| PointOfInteraction | Component                           |  |
| PointOfInteraction | ComponentIdentification             |  |
| PointOfInteraction | GroupIdentifier                     |  |
| PointOfInteraction | LineWidth                           |  |
| PointOfInteraction | NumberOfLines                       |  |
| PointOfInteraction | ErrorLog                            |  |
| PointOfInteraction | ComponentVersionNumber              |  |
| PointOfInteraction | ControllingTerminalManagementSystem |  |
|                    |                                     |  |

| Portfolio          |                  |  |
|--------------------|------------------|--|
| Portfolio          | Valuation        |  |
| Portfolio          | Transfer         |  |
| Portfolio          | AssetDescription |  |
| Portfolio          | Name             |  |
| Portfolio          | Identification   |  |
| Portfolio          | Strategy         |  |
| Portfolio          | Benchmark        |  |
| Portfolio          | InvestmentPlan   |  |
| Portfolio          | Account          |  |
| PortfolioBenchmark |                  |  |
| PortfolioBenchmark | Index            |  |
| PortfolioBenchmark | Portfolio        |  |
|                    |                  |  |

| PortfolioBenchmark   | BenchmarkWeight         |                |
|----------------------|-------------------------|----------------|
| PortfolioBenchmark   | MaximumDeviation        |                |
| PortfolioBenchmark   | MinimumDeviation        |                |
| PortfolioBenchmark   | EffectivePeriod         |                |
| PortfolioBenchmark   | Description             |                |
| PortfolioBenchmark   | Approver                |                |
| PortfolioBenchmark   | Administrator           |                |
| PortfolioManagerRole |                         | AssetPartyRole |
| PortfolioStrategy    |                         |                |
| PortfolioStrategy    | Portfolio               |                |
| PortfolioStrategy    | InclusionIndicator      |                |
| PortfolioStrategy    | MinimumInvestmentAmount |                |
|                      |                         |                |

| PortfolioStrategy           | MinimumInvestmentRate   | Minimum percentage that has to<br>be invested in the specified<br>PercentageRate<br>strategy.                          |
|-----------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------|
| PortfolioStrategy           | MaximumInvestmentAmount | Maximum amount that may be<br>CurrencyAndAmount<br>invested in the specified strategy.                                 |
| PortfolioStrategy           | MaximumInvestmentRate   | Maximum percentage that may<br>be invested in the specified<br>PercentageRate<br>strategy.                             |
| PortfolioStrategy           | EffectivePeriod         | Period during which the<br>DateTimePeriod<br>investment guideline is valid.                                            |
| PortfolioStrategy           | DistributionPolicy      | Income policy relating to the<br>fund, ie, if income is paid out or<br>DistributionPolicyCode<br>retained in the fund. |
| PortfolioStrategy           | Description             | Free text description of the<br>investment guideline, for<br>Max2000Text<br>example, rating requirements.              |
| PortfolioStrategy           | Definition              | Definition of the portfolio<br>PortfolioStrategyDefinition<br>strategy.                                                |
| PortfolioStrategyDefinition |                         | Additional information on the<br>definition of the strategy.                                                           |
| PortfolioStrategyDefinition | Strategy                | Stategy attached to the portfolio.<br>PortfolioStrategy                                                                |
| PortfolioStrategyDefinition | Name                    | Name of the defined strategy.<br>Max350Text                                                                            |
| PortfolioStrategyDefinition | Description             | Free text description of the<br>Max350Text<br>strategy definition.                                                     |
| PortfolioStrategyDefinition | EffectivePeriod         | Period during which the defined<br>DateTimePeriod<br>strategy is valid.                                                |

| PortfolioTransfer |                              |  |
|-------------------|------------------------------|--|
| PortfolioTransfer | TransferredYear              |  |
| PortfolioTransfer | CashComponentIndicator       |  |
| PortfolioTransfer | AccountFrom                  |  |
| PortfolioTransfer | AccountTo                    |  |
| PortfolioTransfer | PaymentObligation            |  |
| PortfolioTransfer | TransferredPortfolio         |  |
| PortfolioTransfer | SecuritiesDeliveryObligation |  |
| PortfolioTransfer | TransferredAmount            |  |
|                   |                              |  |

| PortfolioTransfer  | TransferredPercentage |  |
|--------------------|-----------------------|--|
| PortfolioTransfer  | TransferDate          |  |
| PortfolioTransfer  | NomineeAccount        |  |
| PortfolioTransfer  | PEPOrISAPlan          |  |
| PortfolioTransfer  | CurrentYearISAType    |  |
| PortfolioValuation |                       |  |
| PortfolioValuation | TotalPortfolioValue   |  |
| PortfolioValuation | TotalBookValue        |  |
| PortfolioValuation | TotalReceipts         |  |
| PortfolioValuation | TotalDisbursements    |  |
| PortfolioValuation | IncomeReceived        |  |
|                    |                       |  |

| PortfolioValuation | ExpensesPaid          |
|--------------------|-----------------------|
| PortfolioValuation | Portfolio             |
| PortfolioValuation | ValuationPeriod       |
| Position           |                       |
| Position           | NetQuantity           |
| Position           | NetPositionAmount     |
| Position           | System                |
|                    |                       |
| Position           | Price                 |
| Position           | SecuritiesSettlement  |
| Position           | InitialPositionAmount |
| PostTradeEvent     |                       |
| PostTradeEvent     | Type                  |

| PostTradeEvent<br>ProfitOrLossSettlementDate<br>PostTradeEvent<br>ProfitOrLoss<br>PostTradeEvent<br>OutstandingSettlementAmount<br>PostTradeRiskReduction<br>PostTradeRiskReduction<br>Structurer<br>PostTradeRiskReduction<br>Technique<br>PostTradeRiskReduction<br>PTRRIdentifier<br>PostTradeRiskReduction<br>RelatedDerivativeEvent<br>PostTradeRiskReduction<br>ServiceProvider<br>PostalAddress<br>ContactPoint | PostTradeEvent | UnderlyingLiabilityReference |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|------------------------------|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                        |                |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |                |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |                |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |                |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |                |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |                |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |                |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |                |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |                |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |                |                              |  |

| PostalAddress | AddressType                  |  |
|---------------|------------------------------|--|
| PostalAddress | StreetName                   |  |
| PostalAddress | StreetBuildingIdentification |  |
| PostalAddress | PostCodeIdentification       |  |
| PostalAddress | TownName                     |  |
| PostalAddress | BuildingName                 |  |
| PostalAddress | Floor                        |  |
| PostalAddress | PostOfficeBox                |  |
| PostalAddress | Department                   |  |
| PostalAddress | SubDepartment                |  |
| PostalAddress | Location                     |  |
| PostalAddress | ChequeIssue                  |  |
| PostalAddress | Country                      |  |

| PostalAddress | ValidityPeriod          |  |
|---------------|-------------------------|--|
| PostalAddress | SuiteIdentification     |  |
| PostalAddress | BuildingIdentification  |  |
| PostalAddress | MailDeliverySubLocation |  |
| PostalAddress | Block                   |  |
| PostalAddress | Lot                     |  |
| PostalAddress | MailingInstructions     |  |
| PostalAddress | PhysicalDelivery        |  |
| PostalAddress | UnitNumber              |  |
| PostalAddress | CareOf                  |  |
|               |                         |  |

| PowerOfAttorney             |                             | Mandate |
|-----------------------------|-----------------------------|---------|
| PowerOfAttorney             | AuthorisedParty             |         |
| PowerOfAttorney             | PowerOfAttorneyRequirements |         |
| PowerOfAttorney             | AuthorisedAccount           |         |
| PowerOfAttorneyRequirements |                             |         |
| PowerOfAttorneyRequirements | LegalRequirement            |         |
| PowerOfAttorneyRequirements | OtherDocumentation          |         |
| PowerOfAttorneyRequirements | PowerOfAttorney             |         |
| PowerOfAttorneyRequirements | Meeting                     |         |
| PrePaymentSpeed             |                             |         |
| PrePaymentSpeed             | Type                        |         |

| PrePaymentSpeed    | Rate                          |
|--------------------|-------------------------------|
| PremiumCalculation |                               |
| PremiumCalculation | Option                        |
| PremiumCalculation | PercentageOfCallAmount        |
| PremiumCalculation | PercentageOfPutAmount         |
| PremiumCalculation | PointsOfCallAmount            |
| PremiumCalculation | PointsOfPutAmount             |
| Presentation       |                               |
| Presentation       | CommunicationMethod           |
| Presentation       | PresentedUndertaking          |
| Presentation       | Medium                        |
| Presentation       | PresentedDocument             |
| Presentation       | ElectronicPresentationAddress |

| Presentation | PresentationDate  |  |
|--------------|-------------------|--|
| Presentation | ApplicableChannel |  |
| Price        |                   |  |
| Price        | Amount            |  |
| Price        | Option            |  |
| Price        | UnitPriceProduct  |  |
| Price        | NetPriceProduct   |  |
| Price        | PriceAdjustment   |  |
| Price        | GrossPriceProduct |  |
| Price        | UnitOfMeasure     |  |
| Price        | PriceTolerance    |  |
| Price        | Currency          |  |
|              |                   |  |

| Price                    | Factor                 |                            |
|--------------------------|------------------------|----------------------------|
| Price                    | Netting                |                            |
| Price                    | SecuritiesPricing      |                            |
| Price                    | RelatedEnergy          |                            |
| PrimaryOwner             |                        | InvestmentAccountPartyRole |
| PrimaryPlaceOfDeposit    |                        | SecuritiesPartyRole        |
| PrincipalCollectionAgent |                        | SecuritiesPartyRole        |
| PrincipalPayingAgent     |                        | SecuritiesPartyRole        |
| PrivateCertificate       |                        | Document                   |
| PrivateCertificate       | CertificateType        |                            |
| PrivateCertificate       | CertificationIndicator |                            |

| PrivateCertificate | CheckingDate            |  |
|--------------------|-------------------------|--|
| PrivateCertificate | CheckingFrequency       |  |
| PrivateCertificate | NextRevisionDate        |  |
| PrivateCertificate | Person                  |  |
| ProceedsDefinition |                         |  |
| ProceedsDefinition | SpecialConcessionAmount |  |
| ProceedsDefinition | CreditDebitIndicator    |  |
| ProceedsDefinition | EarliestPaymentDate     |  |
| ProceedsDefinition | ValueDate               |  |

| ProceedsDefinition | NonEligibleProceedsIndicator     |                       | Specifies information regarding<br>outturn resources that cannot be<br>processed by the CSD. Special<br>delivery instruction is required<br>from the account owner for the<br>CA outcome to be credited. | NonEligibleProceedsIndicatorCode |                    |
|--------------------|----------------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|--------------------|
| ProceedsDefinition | IssuerOfferorTaxabilityIndicator | the issuer / offeror. | Proceeds are taxable according<br>to the information provided by                                                                                                                                         | Max35Text                        |                    |
| ProceedsDefinition | OfferPriceFixingDate             |                       | Date/time at which an offer price<br>is determined (as compared to<br>its reset date if applicable).                                                                                                     | ISODateTime                      |                    |
| ProceedsDefinition | Option                           | specified.            | Option for which proceeds are                                                                                                                                                                            | CorporateActionOption            | ProceedsDefinition |
| ProceedsDefinition | CorporateAction                  |                       | Corporate action for which the<br>proceeds are specified.                                                                                                                                                | CorporateActionEvent             | ProceedsDefinition |
| ProceedsDefinition | CountryOfIncomeSource            |                       | Indicates the country from which<br>the income originates.                                                                                                                                               | CountryCode                      |                    |
| Product            |                                  | goods.                | Item that is offered for sale.<br>Products can be services or                                                                                                                                            |                                  |                    |
| Product            | CardPayment                      |                       | Card payment for which a<br>product was specified.                                                                                                                                                       | CardPayment                      |                    |
| Product            | UnitPrice                        |                       | Price per unit of product.                                                                                                                                                                               | Price                            |                    |
| Product            | ProductCategory                  |                       | Category of the product.                                                                                                                                                                                 | ProductCategory                  |                    |
| Product            | LineItem                         |                       | Specifies the line item in which<br>the product is specified.                                                                                                                                            | LineItem                         |                    |
| Product            | ProductIdentification            |                       | Identification of the product.                                                                                                                                                                           | ProductIdentification            |                    |
|                    |                                  |                       |                                                                                                                                                                                                          |                                  |                    |

| Product<br>Name<br>Product<br>Description<br>Product<br>Origin |
|----------------------------------------------------------------|
|                                                                |
|                                                                |
|                                                                |
| Product<br>Characteristics                                     |
| Product<br>NetPrice                                            |
| Product<br>Quantity                                            |
| Product<br>GrossPrice                                          |
| Product<br>Quality                                             |
| Product<br>Delivery                                            |
| Product<br>PurchaseOrder                                       |
| Product<br>Tax                                                 |
| ProductCategory                                                |
| ProductCategory<br>Product                                     |

| ProductCategory        | Type                         |                      |
|------------------------|------------------------------|----------------------|
| ProductCategory        | Category                     |                      |
| ProductCategory        | RelatedCardPaymentValidation |                      |
| ProductCharacteristics |                              |                      |
| ProductCharacteristics | Product                      |                      |
| ProductCharacteristics | Characteristics              |                      |
| ProductCharacteristics | Type                         |                      |
| ProductDelivery        |                              | ObligationFulfilment |
| ProductDelivery        | DeliveryPeriod               |                      |
| ProductDelivery        | Routing                      |                      |
| ProductDelivery        | TradeSettlement              |                      |
| ProductDelivery        | Obligation                   |                      |
|                        |                              |                      |

| ProductDelivery           | TradeCertificate      |            |
|---------------------------|-----------------------|------------|
| ProductDelivery           | InsuranceCertificate  |            |
| ProductDelivery           | Product               |            |
| ProductDeliveryObligation |                       | Obligation |
| ProductDeliveryObligation | ProductDeliveryOffset |            |
| ProductDeliveryObligation | CommercialTrade       |            |
| ProductIdentification     |                       |            |
| ProductIdentification     | Identifier            |            |
| ProductIdentification     | Product               |            |
| ProductIdentification     | Type                  |            |
|                           |                       |            |

| ProductIdentification | GlobalSerialIdentifier            |  |
|-----------------------|-----------------------------------|--|
| ProductQuantity       |                                   |  |
| ProductQuantity       | UnitOfMeasure                     |  |
| ProductQuantity       | Value                             |  |
| ProductQuantity       | Product                           |  |
| ProductQuantity       | Factor                            |  |
| ProductQuantity       | NetWeightRelatedLineItem          |  |
| ProductQuantity       | BilledQuantityRelatedLineItem     |  |
| ProductQuantity       | RelatedPackaging                  |  |
| ProductQuantity       | PackagingForUnitQuantity          |  |
| ProductQuantity       | ChargeFreeQuantityRelatedLineItem |  |

| ProductQuantity | MeasureQuantityStart              |                  |
|-----------------|-----------------------------------|------------------|
| ProductQuantity | MeasureQuantityEnd                |                  |
| ProductQuantity | QuantityTolerance                 |                  |
| ProductQuantity | PackagingForConsignmentlQuantity  |                  |
| ProductQuantity | PackagingForVolume                |                  |
| ProductQuantity | PackagingForWeight                |                  |
| ProductQuantity | GrossPriceQuantityRelatedLineItem |                  |
| ProductQuantity | NetPriceQuantityRelatedLineItem   |                  |
| ProductQuantity | GrossWeightRelatedLineItem        |                  |
| ProductQuantity | TimeUnit                          |                  |
| ProxyAgent      |                                   | MeetingPartyRole |

| ProxyAppointment          |                             |                  |
|---------------------------|-----------------------------|------------------|
| ProxyAppointment          | ProxyType                   |                  |
| ProxyAppointment          | RelatedMeetingInstruction   |                  |
| ProxyAppointment          | Identification              |                  |
| ProxyAppointment          | Vote                        |                  |
| ProxyAppointment          | AdditionalParticipationCost |                  |
| ProxyAppointmentCondition |                             |                  |
| ProxyAppointmentCondition | NotificationAddress         |                  |
| ProxyAppointmentCondition | Meeting                     |                  |
| ProxyAppointmentCondition | RegistrationMethod          |                  |
| ProxyAppointmentCondition | AllowedProxyType            |                  |
| ProxyAppointmentDeadline  |                             | MeetingDeadline  |
| ProxyAssignerRole         |                             | MeetingPartyRole |

| PurchaseOrder                |                                                            | Order          |
|------------------------------|------------------------------------------------------------|----------------|
| PurchaseOrder                | TotalAmount                                                |                |
| PurchaseOrder                | ResultingCommercialTrade                                   |                |
| PurchaseOrder                | Product                                                    |                |
| PurchaseOrder                | Identification                                             |                |
| QualifiedForeignIntermediary |                                                            | TradePartyRole |
| QualifiedForeignIntermediary | Country                                                    |                |
| QuantityRatio                |                                                            |                |
| QuantityRatio                | AdditionalQuantityForResultantSecuritiesProceedsDefinition |                |
| QuantityRatio                | Quantity1                                                  |                |
| QuantityRatio                | Quantity2                                                  |                |

| QuantityRatio<br>AdditionalQuantityForSubscribedSecuritiesProceedsDefinition<br>QuantityRatio<br>NewToOldProceedsDefinition<br>QuantityRatio<br>NewToUnderlyingProceedsDefinition<br>QuantityRatio<br>IntermediateSecuritiesProceedsDefinition<br>QuantityRatio<br>Warrant<br>Quorum<br>Quorum<br>Quantity<br>Quorum<br>Percentage<br>Quorum<br>QuorumRequired<br>Quorum<br>Meeting |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                     |  |  |

| Quote |                      |  |
|-------|----------------------|--|
| Quote | MaximumQuantity      |  |
| Quote | Quantity             |  |
| Quote | MinimumQuantity      |  |
| Quote | PartyRole            |  |
| Quote | RelatedNegotiation   |  |
| Quote | QuotedRate           |  |
| Quote | PreviousClosingPrice |  |
| Quote | RequestedPrice       |  |
| Quote | Price                |  |
|       |                      |  |

| Quote           | MarketPrice            |
|-----------------|------------------------|
| Quote           | MidSideQuoteVariable   |
| Quote           | BidSideQuoteVariable   |
| Quote           | OfferSideQuoteVariable |
| Quote           | SecurityQuoteVariable  |
| Quote           | QuoteSwap              |
| Quote           | ValidUntilDateTime     |
| Quote           | Currency               |
| Quote           | Status                 |
| Quote           | QuotedSecurity         |
| QuoteOriginator | InformationPartyRole   |
| QuoteOriginator | QuoteOriginatorType    |

| QuoteRequestor     |                                             | InformationPartyRole |
|--------------------|---------------------------------------------|----------------------|
| QuoteRequestor     | RequestorEligibility                        |                      |
| QuoteStatus        |                                             | Status               |
| QuoteStatus        | Status                                      |                      |
| QuoteStatus        | RejectionReason                             |                      |
| QuoteStatus        | RelatedQuote                                |                      |
| QuotingInstitution |                                             | InformationPartyRole |
| RateAndAmount      |                                             |                      |
| RateAndAmount      | FinalDividendParameters                     |                      |
| RateAndAmount      | FullyFrankedRateAndAmountDividendParameters |                      |
| RateAndAmount      | GrossDividendParameters                     |                      |
| RateAndAmount      | Amount                                      |                      |
| RateAndAmount      | Index                                       |                      |
|                    |                                             |                      |

| RateAndAmount | NetDividendParameters                         |  |
|---------------|-----------------------------------------------|--|
| RateAndAmount | MaximumAllowedBiddingConditions               |  |
| RateAndAmount | ProvisionalDividendParameters                 |  |
| RateAndAmount | SolicitationFeeCorporateActionParameters      |  |
| RateAndAmount | Rate                                          |  |
| RateAndAmount | RateBiddingConditions                         |  |
| RateAndAmount | SecuritiesTax                                 |  |
| RateAndAmount | EarlySolicitationFeeCorporateActionParameters |  |
| RateAndAmount | InterestRelatedIssuance                       |  |
| RateAndAmount | LossRelatedIssuance                           |  |
| RateAndAmount | AbsoluteValue                                 |  |
| RateAndAmount | Operator                                      |  |
| RateAndAmount | RelatedYieldCalculation                       |  |
|               |                                               |  |

| RateAndAmount      | ConduitForeignIncomeAmountDividendParameters |                               |
|--------------------|----------------------------------------------|-------------------------------|
| RateAndAmount      | DeemedAmountDividendParameters               |                               |
| Rating             |                                              |                               |
| Rating             | Security                                     |                               |
| Rating             | RatingScheme                                 |                               |
| Rating             | ValueDate                                    |                               |
| Rating             | Value                                        |                               |
| Reassignment       |                                              | InvestigationResolution       |
| Reassignment       | Justification                                |                               |
| Reassignment       | ReassignedCase                               |                               |
| ReceiversCustodian |                                              | SecuritiesSettlementPartyRole |
|                    |                                              |                               |

| ReceiversIntermediary    |                          | SecuritiesSettlementPartyRole |
|--------------------------|--------------------------|-------------------------------|
| ReceivingAgent           |                          | SecuritiesSettlementPartyRole |
| ReceivingDepositoryRole  |                          | ReceivingSettlementParty      |
| ReceivingSettlementParty |                          | SecuritiesSettlementPartyRole |
| ReceivingSettlementParty | ReceivingSettlementParty |                               |
| ReceivingSettlementParty | NextParty                |                               |

| RecipientBank             |                              | CommercialTradePartyRole |
|---------------------------|------------------------------|--------------------------|
| Reconciliation            |                              |                          |
| Reconciliation            | System                       |                          |
| Reconciliation            | Document                     |                          |
| Reconciliation            | ReconciledTrades             |                          |
| Reconciliation            | Account                      |                          |
| ReconciliationTransaction |                              | Reconciliation           |
| ReconciliationTransaction | ReconciliationIdentification |                          |
| ReconciliationTransaction | Currency                     |                          |
| ReconciliationTransaction | TransactionType              |                          |

| ReconciliationTransaction | TotalNumber                        |                              |
|---------------------------|------------------------------------|------------------------------|
| ReconciliationTransaction | CumulativeAmount                   |                              |
| ReconciliationTransaction | ClosePeriod                        |                              |
| ReconciliationTransaction | CardPaymentTotal                   |                              |
| RedemptionExecution       |                                    | InvestmentFundOrderExecution |
| RedemptionExecution       | RedeemedNetAmount                  |                              |
| RedemptionExecution       | PartialRedemptionWithholdingAmount |                              |
| RedemptionExecution       | SettlementDate                     |                              |
| RedemptionOrder           |                                    | InvestmentFundOrder          |
| RedemptionOrder           | HoldingsRedemptionRate             |                              |
| RedemptionSchedule        |                                    |                              |

| RedemptionSchedule | BusinessDayConvention |  |
|--------------------|-----------------------|--|
| RedemptionSchedule | EffectivePeriod       |  |
| RedemptionSchedule | PriceChange           |  |
| RedemptionSchedule | Price                 |  |
| RedemptionSchedule | PartyType             |  |
| RedemptionSchedule | AmountFulfilType      |  |
| RedemptionSchedule | MinimumNoticeDays     |  |
| RedemptionSchedule | MaximumNoticeDays     |  |
| RedemptionSchedule | FinancialCenter       |  |
| RedemptionSchedule | NoticePeriodType      |  |

| RedemptionSchedule | PriceChangeFrequency |          |
|--------------------|----------------------|----------|
| RedemptionSchedule | PriceFrequency       |          |
| RedemptionSchedule | Security             |          |
| RegisteredContract |                      | Contract |
| RegisteredContract | Certificate          |          |
| RegisteredContract | ContractBalance      |          |
| RegisteredContract | ReportingParty       |          |
| RegisteredContract | Identification       |          |
| RegisteredContract | DeliveryDate         |          |
| RegisteredContract | RegistrationAgent    |          |
| RegisteredContract | ReceivingParty       |          |
|                    |                      |          |

| RegisteredContract | Priority            |                     |
|--------------------|---------------------|---------------------|
| RegisteredContract | RegistrationDate    |                     |
| RegisteredContract | ClosureReason       |                     |
| RegisteredContract | ClosureDate         |                     |
| RegisteredContract | PaymentScheduleType |                     |
| RegisteredContract | SubmissionDate      |                     |
| RegisteredContract | SendingParty        |                     |
| RegisteredContract | DeliveryMethod      |                     |
| RegisteredContract | SubmissionMethod    |                     |
| RegisteredContract | RelatedPayment      |                     |
| RegisteredContract | Attachment          |                     |
| RegistrarRole      |                     | SecuritiesPartyRole |

| RegistrarRole           | RegistrarAccount              |                  |
|-------------------------|-------------------------------|------------------|
| RegistrarRole           | RegisterName                  |                  |
| RegistrationBeneficiary |                               | MeetingPartyRole |
| RegulatoryAuthorityRole |                               | Role             |
| RegulatoryAuthorityRole | RegulatoryReport              |                  |
| RegulatoryAuthorityRole | Country                       |                  |
| RegulatoryReport        |                               |                  |
| RegulatoryReport        | DebitCreditReportingIndicator |                  |
| RegulatoryReport        | Authority                     |                  |
| RegulatoryReport        | Code                          |                  |

| RegulatoryReport        | Amount                |      |
|-------------------------|-----------------------|------|
| RegulatoryReport        | Description           |      |
| RegulatoryReport        | Type                  |      |
| RegulatoryReport        | Date                  |      |
| RegulatoryReport        | ReportedTransaction   |      |
| RegulatoryReport        | UnderlyingProduct     |      |
| RegulatoryReport        | NonStandardFlag       |      |
| RegulatoryReport        | ReportingPartyRole    |      |
| RegulatoryReportingRole |                       | Role |
| RegulatoryReportingRole | RelatedReportingParty |      |
|                         |                       |      |

| RegulatoryReportingRole | RelatedRegistrationAgent        |                     |
|-------------------------|---------------------------------|---------------------|
| RegulatoryReportingRole | RelatedReceivingParty           |                     |
| RegulatoryReportingRole | RelatedSendingParty             |                     |
| Reinvestment            |                                 |                     |
| Reinvestment            | RelatedinvestmentAccountService |                     |
| Reinvestment            | InvestmentFundClass             |                     |
| Reinvestment            | Percentage                      |                     |
| RemarketingAgent        |                                 | SecuritiesPartyRole |
| ReportingPartyRole      |                                 | Role                |
| ReportingPartyRole      | RegulatoryReport                |                     |
| ReportingService        |                                 | AccountService      |
|                         |                                 |                     |

| ReportingService      | StatementFrequency              |                  |
|-----------------------|---------------------------------|------------------|
| ReportingService      | FloorNotificationAmount         |                  |
| ReportingService      | CeilingNotificationAmount       |                  |
| ReportingService      | ReportingChannel                |                  |
| ReportingService      | RelatedInvestmentAccountService |                  |
| RepresentativeOfficer |                                 | AccountPartyRole |
| RepresentativeOfficer | Organisation                    |                  |

| RepurchaseAgreement |                              | SecuritiesFinancing |
|---------------------|------------------------------|---------------------|
| RepurchaseAgreement | PaymentObligation            |                     |
| Reservation         |                              | Limit               |
| Reservation         | ReservationType              |                     |
| Reservation         | RelatedIntraPositionTransfer |                     |
| Reservation         | SettlementInstruction        |                     |
| Reservation         | AccountService               |                     |
| Resolution          |                              |                     |
| Resolution          | IssuerLabel                  |                     |
|                     |                              |                     |

| Resolution | Description                  |  |
|------------|------------------------------|--|
| Resolution | Title                        |  |
| Resolution | Type                         |  |
| Resolution | ForInformationOnly           |  |
| Resolution | SubmittedBySecurityHolder    |  |
| Resolution | ManagementRecommendation     |  |
| Resolution | NotifyingPartyRecommendation |  |
| Resolution | CastVotes                    |  |
| Resolution | Meeting                      |  |
| Resolution | VoteOptions                  |  |
| Resolution | VoteType                     |  |
|            |                              |  |

| Resolution                 | VotingRightsThresholdForApproval      |                 |
|----------------------------|---------------------------------------|-----------------|
| Resolution                 | ThresholdBasis                        |                 |
| ResolutionProposal         |                                       |                 |
| ResolutionProposal         | ResolutionProposalThreshold           |                 |
| ResolutionProposal         | ResolutionProposalThresholdPercentage |                 |
| ResolutionProposal         | Meeting                               |                 |
| ResolutionProposalDeadline |                                       | MeetingDeadline |
| Response                   |                                       |                 |
| Response                   | ResponseReason                        |                 |
| Response                   | RelatedCardPaymentValidation          |                 |
|                            |                                       |                 |

| Response             | ResponseToAuthorisation |                   |
|----------------------|-------------------------|-------------------|
| ResponsiblePartyRole |                         | DocumentPartyRole |
| RightsHolder         |                         | MeetingPartyRole  |
| RiskManagementLimit  |                         | Limit             |
| RiskManagementLimit  | CashManagementService   |                   |
| RiskManagementLimit  | Counterparty            |                   |
| Role                 |                         |                   |
| Role                 | Player                  |                   |

| Role               | ContactPersonRole        |                      |
|--------------------|--------------------------|----------------------|
| Role               | PartyRole                |                      |
| Role               | CounterpartyRisk         |                      |
| Role               | Entry                    |                      |
| RolePlayer         |                          |                      |
| RolePlayer         | Role                     |                      |
| RolePlayer         | ValidityPeriod           |                      |
|                    |                          |                      |
| Rollover           |                          | ObligationFulfilment |
| Rollover           | SecuritiesSettlement     |                      |
| RoundingParameters |                          |                      |
| RoundingParameters | InvestmentAccountService |                      |
| RoundingParameters | RoundingModulus          |                      |

| RoundingParameters  | RoundingDirection           |                     |
|---------------------|-----------------------------|---------------------|
| RoundingParameters  | RelatedPegOrderInstruction  |                     |
| SSIDatabaseProvider |                             | SettlementPartyRole |
| SSIDatabaseProvider | StandingSettlementDatabase  |                     |
| SafekeepingPlace    |                             | SecuritiesPartyRole |
| SafekeepingPlace    | SafekeepingPlaceType        |                     |
| SafekeepingPlace    | Country                     |                     |
| SafekeepingPlace    | RelatedSecuritiesAccount    |                     |
| SafekeepingPlace    | SecuritiesBalance           |                     |
| SafekeepingPlace    | SecuritiesSettlement        |                     |
| SafekeepingPlace    | DigitalLedgerIdentification |                     |

| Scheme |                          |  |
|--------|--------------------------|--|
| Scheme | NameShort                |  |
| Scheme | Code                     |  |
| Scheme | Identification           |  |
| Scheme | Rating                   |  |
| Scheme | CreditorRole             |  |
| Scheme | InformationPartyRole     |  |
| Scheme | Version                  |  |
| Scheme | AssessmentValidityPeriod |  |
| Scheme | NameLong                 |  |
| Scheme | Description              |  |
| Scheme | DomainValueCode          |  |
|        |                          |  |

| Scheme         | DomainValueName     |                            |
|----------------|---------------------|----------------------------|
| Scheme         | Sector              |                            |
| Scheme         | AssetClassification |                            |
| SchemeOwner    |                     | InformationPartyRole       |
| SecondaryOwner |                     | InvestmentAccountPartyRole |
| Sector         |                     |                            |
| Sector         | Security            |                            |
| Sector         | Scheme              |                            |
| Sector         | Organisation        |                            |
| Sector         | Identification      |                            |
| Sector         | Strategy            |                            |

| SectorStrategy    |                          | PortfolioStrategy |
|-------------------|--------------------------|-------------------|
| SectorStrategy    | Sector                   |                   |
| SecuritiesAccount |                          | Account           |
| SecuritiesAccount | SecuritiesAccountType    |                   |
| SecuritiesAccount | RelatedInvestmentAccount |                   |
| SecuritiesAccount | RelatedTransfer          |                   |
| SecuritiesAccount | SecuritiesPartyRole      |                   |
| SecuritiesAccount | Security                 |                   |
| SecuritiesAccount | RelatedRegistrar         |                   |
| SecuritiesAccount | SafekeepingPlace         |                   |
| SecuritiesAccount | SecuritiesBalance        |                   |
| SecuritiesAccount | CorporateActionServicing |                   |

| SecuritiesAccount<br>RelatedAllocation                               |
|----------------------------------------------------------------------|
| SecuritiesAccount<br>SecuritiesEntry                                 |
| SecuritiesAccount<br>ClearingAccountOwner                            |
| SecuritiesAccount<br>MarginAccountOwner                              |
| SecuritiesAccount<br>DeliveryAccountOwner                            |
| SecuritiesAccount<br>RelatedPowerOfAttorney                          |
| SecuritiesAccount<br>RelatedMeetingInstruction                       |
| SecuritiesAccount<br>ClearingAccountType                             |
| SecuritiesAccount<br>RelatedOrder                                    |
| SecuritiesAccount<br>DisclosedListTrading                            |
| SecuritiesAccount<br>AccountLink                                     |
| SecuritiesAndCashDistribution<br>Distribution                        |
| SecuritiesAndCashDistribution<br>IntermediateToUnderlyingDenominator |

| SecuritiesAndCashDistribution | MaximumHolding                     |  |
|-------------------------------|------------------------------------|--|
| SecuritiesAndCashDistribution | MaximumExercisableQuantity         |  |
| SecuritiesAndCashDistribution | MinimumExercisableQuantity         |  |
| SecuritiesAndCashDistribution | DistributedToUnderlyingDenominator |  |
| SecuritiesAndCashDistribution | IntermediateToUnderlyingNumerator  |  |
| SecuritiesAndCashDistribution | MinimumHolding                     |  |
| SecuritiesAndCashDistribution | DistributedToUnderlyingNumerator   |  |
| SecuritiesAndCashDistribution | SecuritiesDistribution             |  |
| SecuritiesAndCashDistribution | CashDistribution                   |  |
|                               |                                    |  |

| SecuritiesBalance |                                     | Balance |
|-------------------|-------------------------------------|---------|
| SecuritiesBalance | NetGainLoss                         |         |
| SecuritiesBalance | SecuritiesAccount                   |         |
| SecuritiesBalance | EligibleBalanceRelatedEntitlement   |         |
| SecuritiesBalance | ShortLong                           |         |
| SecuritiesBalance | AggregateQuantity                   |         |
| SecuritiesBalance | CorporateActionEntitlement          |         |
| SecuritiesBalance | InstructedBalanceRelatedEntitlement |         |
|                   |                                     |         |

| SecuritiesBalance | UninstructedBalanceRelatedEntitlement |  |
|-------------------|---------------------------------------|--|
| SecuritiesBalance | MainSecuritiesBalance                 |  |
| SecuritiesBalance | SecuritiesSubBalance                  |  |
| SecuritiesBalance | SecuritiesBalanceType                 |  |
| SecuritiesBalance | SubBalanceQuantity                    |  |
| SecuritiesBalance | Security                              |  |
| SecuritiesBalance | ExchangeRate                          |  |
| SecuritiesBalance | AvailabilityIndicator                 |  |
| SecuritiesBalance | AvailableQuantity                     |  |

| SecuritiesBalance          | RelatedMeetingEntitlement            |          |
|----------------------------|--------------------------------------|----------|
| SecuritiesBalance          | UnavailableQuantity                  |          |
| SecuritiesBalance          | SafekeepingPlace                     |          |
| SecuritiesBalance          | SecuritiesEntry                      |          |
| SecuritiesBalance          | NotEligibleBalanceRelatedEntitlement |          |
| SecuritiesBalance          | RelatedIntraPositionTransfer         |          |
| SecuritiesBalance          | CostAdjustment                       |          |
| SecuritiesBalance          | Pledgee                              |          |
| SecuritiesBlockingDeadline |                                      | Deadline |
| SecuritiesBlockingDeadline | BlockingPeriod                       |          |
| SecuritiesCertificate      |                                      |          |
|                            |                                      |          |

| SecuritiesCertificate | Number               |          |
|-----------------------|----------------------|----------|
| SecuritiesCertificate | BasicRegistration    |          |
| SecuritiesCertificate | RelatedDelivery      |          |
| SecuritiesClearing    |                      | Clearing |
| SecuritiesClearing    | SecuritiesSettlement |          |
| SecuritiesClearing    | BuyIn                |          |
| SecuritiesClearing    | Novation             |          |
| SecuritiesClearing    | Netting              |          |
| SecuritiesConversion  |                      |          |
| SecuritiesConversion  | ConversionPrice      |          |
| SecuritiesConversion  | ConversionDate       |          |

| SecuritiesConversion | MinimumExercisableQuantity         |  |
|----------------------|------------------------------------|--|
| SecuritiesConversion | MinimumExercisableMultipleQuantity |  |
| SecuritiesConversion | MaximumExercisableQuantity         |  |
| SecuritiesConversion | ConversionType                     |  |
| SecuritiesConversion | ConversionPeriod                   |  |
| SecuritiesConversion | ConversionRatioDenominator         |  |
| SecuritiesConversion | ConversionRatioNumerator           |  |
| SecuritiesConversion | Ratio                              |  |
| SecuritiesConversion | ConversionUnitCurrency             |  |
| SecuritiesConversion | RelatedOption                      |  |
|                      |                                    |  |

| SecuritiesConversion | BusinessDayConvention              |  |
|----------------------|------------------------------------|--|
| SecuritiesConversion | ConversionChoice                   |  |
| SecuritiesConversion | ConversionFixedExchangeRate        |  |
| SecuritiesConversion | ConversionMarginAmount             |  |
| SecuritiesConversion | ConversionOption                   |  |
| SecuritiesConversion | ConversionQuotedCurrency           |  |
| SecuritiesConversion | FinancialCenter                    |  |
| SecuritiesConversion | MinimumNoticeDays                  |  |
| SecuritiesConversion | NoticePeriodType                   |  |
| SecuritiesConversion | ProtectionAgainstDilutionIndicator |  |
|                      |                                    |  |

| SecuritiesConversion         | ReverseConversionIndicator |            |
|------------------------------|----------------------------|------------|
| SecuritiesConversion         | SecurityIdentification     |            |
| SecuritiesConversion         | PartyType                  |            |
| SecuritiesConversion         | ContractSize               |            |
| SecuritiesDeliveryObligation |                            | Obligation |
| SecuritiesDeliveryObligation | CCPEligibility             |            |
| SecuritiesDeliveryObligation | NettingEligibility         |            |
| SecuritiesDeliveryObligation | TransferInstructionDate    |            |
| SecuritiesDeliveryObligation | TransferCurrency           |            |
| SecuritiesDeliveryObligation | RelatedCorporateAction     |            |
| SecuritiesDeliveryObligation | RelatedCollateralMovement  |            |
|                              |                            |            |

| SecuritiesDeliveryObligation | SecuritiesTradeExecution          |              |
|------------------------------|-----------------------------------|--------------|
| SecuritiesDeliveryObligation | RelatedPortfolioTransfer          |              |
| SecuritiesDeliveryObligation | SecuritiesTransfer                |              |
| SecuritiesDeliveryObligation | SettlementInstructionGeneration   |              |
| SecuritiesDeliveryObligation | SettlementDateCode                |              |
| SecuritiesDeliveryObligation | SecuritiesLending                 |              |
| SecuritiesDistribution       |                                   | Distribution |
| SecuritiesDistribution       | MaximumHolding                    |              |
| SecuritiesDistribution       | IntermediateToUnderlyingNumerator |              |

| SecuritiesDistribution | IntermediateToUnderlyingDenominator |  |
|------------------------|-------------------------------------|--|
| SecuritiesDistribution | DistributedToUnderlyingDenominator  |  |
| SecuritiesDistribution | DistributedToUnderlyingNumerator    |  |
| SecuritiesDistribution | MinimumHolding                      |  |
| SecuritiesDistribution | CashFractionsPrice                  |  |
| SecuritiesDistribution | SubscriptionPrice                   |  |
| SecuritiesDistribution | ReinvestmentPrice                   |  |
| SecuritiesDistribution | IntermediateSecurityExpiryDate      |  |
| SecuritiesDistribution | TradingAvailabilityDate             |  |
| SecuritiesDistribution | OfferExpiryDate                     |  |
|                        |                                     |  |

| SecuritiesDistribution | OversubscriptionRate      |  |
|------------------------|---------------------------|--|
| SecuritiesDistribution | OversubscriptionAmount    |  |
| SecuritiesDistribution | ReinvestmentAmount        |  |
| SecuritiesDistribution | ReinvestmentRate          |  |
| SecuritiesDistribution | LoyalityPremiumIndicator  |  |
| SecuritiesDistribution | OversubscriptionIndicator |  |
| SecuritiesDistribution | RenounceableIndicator     |  |
| SecuritiesDistribution | DecimalPrecision          |  |
| SecuritiesDistribution | ReinvestmentType          |  |
| SecuritiesDistribution | RevocableIndicator        |  |
|                        |                           |  |

| SecuritiesDistribution | SecuritiesAndCashDistribution             | Distribution for which the cash<br>distribution elements are<br>SecuritiesAndCashDistribution<br>provided.                                                                   |
|------------------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SecuritiesDistribution | FractionTreatment                         | Specifies how the fractions will<br>RoundingDirectionCode<br>be treated.                                                                                                     |
| SecuritiesDistribution | IntermediateSecurityDistributionIndicator | Indicates whether there will be a<br>distribution of intermediate<br>YesNoIndicator<br>securities or privilege.                                                              |
| SecuritiesEntry        | Entry                                     | Posting to a securities account as<br>a result of a securities creation,<br>deletion or transfer in the context<br>of a securities transaction.                              |
| SecuritiesEntry        | AcquisitionDate                           | Date upon which the investor<br>purchased the financial<br>ISODate<br>instrument.                                                                                            |
| SecuritiesEntry        | FinancialInstrumentQuantity               | Quantity of financial instrument.<br>SecuritiesQuantity                                                                                                                      |
| SecuritiesEntry        | SecuritiesAccount                         | Securities account on which the<br>quantity of the entry is debited<br>or credited. It is derived from the<br>SecuritiesAccount<br>association between Entry and<br>Account. |
| SecuritiesEntry        | SecuritiesBalance                         | Amount that is the result of the<br>sum of the entries from or to an<br>account. It is derived from the<br>SecuritiesBalance<br>association between Entry and<br>Balance.    |
| SecuritiesEntry        | TriggeringSecuritiesTransfer              | Transfer which is at the origin of<br>the entry in the securities<br>SecuritiesTransfer<br>account.                                                                          |

| SecuritiesFinancing |                      | SecuritiesTrade |
|---------------------|----------------------|-----------------|
| SecuritiesFinancing | ReturnLegInstruction |                 |
| SecuritiesFinancing | Type                 |                 |
| SecuritiesFinancing | TerminationDateTime  |                 |
| SecuritiesFinancing | RateChangeDateTime   |                 |
| SecuritiesFinancing | RevaluationIndicator |                 |
| SecuritiesFinancing | InterestPayment      |                 |
| SecuritiesFinancing | VariableRateSupport  |                 |

| SecuritiesFinancing | RepurchaseRate                        |  |
|---------------------|---------------------------------------|--|
| SecuritiesFinancing | StockLoanMargin                       |  |
| SecuritiesFinancing | Interest                              |  |
| SecuritiesFinancing | RepurchaseSpread                      |  |
| SecuritiesFinancing | TransactionCallDelay                  |  |
| SecuritiesFinancing | TotalNumberOfCollateralInstructions   |  |
| SecuritiesFinancing | DealAmount                            |  |
| SecuritiesFinancing | ForfeitRepurchaseAmount               |  |
| SecuritiesFinancing | PremiumAmount                         |  |
| SecuritiesFinancing | TerminationAmountPerPieceOfCollateral |  |

| SecuritiesFinancing | TerminationTransactionAmount |  |
|---------------------|------------------------------|--|
| SecuritiesFinancing | MaturityDateModification     |  |
| SecuritiesFinancing | EarliestCallBackDate         |  |
| SecuritiesFinancing | OpeningSettlementDate        |  |
| SecuritiesFinancing | RepurchaseType               |  |
| SecuritiesFinancing | EndPrice                     |  |
| SecuritiesFinancing | SpreadTransaction            |  |
| SecuritiesFinancing | FinancingAgreement           |  |
| SecuritiesFinancing | OpeningSettlementAmount      |  |

| SecuritiesFinancing          | ClosingLegExecution         |           |
|------------------------------|-----------------------------|-----------|
| SecuritiesFinancing          | OpeningLegExecution         |           |
| SecuritiesFinancing          | RelatedIndicationOfInterest |           |
| SecuritiesFinancing          | Identification              |           |
| SecuritiesFinancing          | TerminationOption           |           |
| SecuritiesFinancingAgreement |                             | Agreement |
| SecuritiesFinancingAgreement | SecuritiesFinancingTrade    |           |
| SecuritiesFinancingAgreement | Currency                    |           |
| SecuritiesFinancingAgreement | TerminationType             |           |
| SecuritiesFinancingAgreement | DeliveryType                |           |
|                              |                             |           |

| SecuritiesFinancingAgreement | MarginRatio            |  |
|------------------------------|------------------------|--|
| SecuritiesIdentification     |                        |  |
| SecuritiesIdentification     | IdentifiedSecurity     |  |
| SecuritiesIdentification     | SecurityIdentification |  |
| SecuritiesIdentification     | RIC                    |  |
| SecuritiesIdentification     | TickerSymbol           |  |
| SecuritiesIdentification     | Bloomberg              |  |
|                              |                        |  |

| SecuritiesIdentification<br>CTA<br>SecuritiesIdentification<br>Common<br>SecuritiesIdentification<br>Name<br>SecuritiesIdentification<br>SEDOL<br>SecuritiesIdentification<br>CUSIP<br>SecuritiesIdentification<br>QUICK |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |

| SecuritiesIdentification | Wertpapier              |  |
|--------------------------|-------------------------|--|
| SecuritiesIdentification | Dutch                   |  |
| SecuritiesIdentification | Valoren                 |  |
| SecuritiesIdentification | Sicovam                 |  |
| SecuritiesIdentification | Belgian                 |  |
| SecuritiesIdentification | IdentificationSuffix    |  |
| SecuritiesIdentification | GenericIdentification   |  |
| SecuritiesIdentification | ValidityPeriod          |  |
| SecuritiesIdentification | ApplicableTradingMarket |  |
| SecuritiesIdentification | PrimeIdentification     |  |
|                          |                         |  |

| SecuritiesIdentification<br>RelatedOtherIdentification<br>SecuritiesIdentification<br>TradingIdentification<br>SecuritiesLending<br>SecuritiesFinancing<br>SecuritiesLending<br>BorrowingFee<br>SecuritiesLending<br>CallableTradeIndicator<br>SecuritiesLending<br>LendingTransactionMethod<br>SecuritiesLending<br>BorrowingReason |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |

| SecuritiesLending      | Reversible                   |  |
|------------------------|------------------------------|--|
| SecuritiesLending      | SecuritiesLendingType        |  |
| SecuritiesLending      | LendingWithCollateral        |  |
| SecuritiesLending      | MinimumDateForCallBack       |  |
| SecuritiesLending      | NumberOfDaysLendingBorrowing |  |
| SecuritiesLending      | PeriodicPayment              |  |
| SecuritiesLending      | Rollover                     |  |
| SecuritiesLending      | BorrowingRate                |  |
| SecuritiesLending      | SecuritiesDeliveryObligation |  |
| SecuritiesModification |                              |  |
|                        |                              |  |

| SecuritiesModification | ChangeType                 |                 |
|------------------------|----------------------------|-----------------|
| SecuritiesModification | NewOrganisationInformation |                 |
| SecuritiesModification | RelatedCorporateEvent      |                 |
| SecuritiesModification | NewSecurityReferenceData   |                 |
| SecuritiesModification | NumberOfSharesIssued       |                 |
| SecuritiesModification | LastTradingDate            |                 |
| SecuritiesOptionTrade  |                            | SecuritiesTrade |
| SecuritiesOptionTrade  | Option                     |                 |
| SecuritiesOrder        |                            | Order           |
| SecuritiesOrder        | OrderEffectiveDate         |                 |
| SecuritiesOrder        | OrderExpiryDate            |                 |

| SecuritiesOrder | Identification   |  |
|-----------------|------------------|--|
| SecuritiesOrder | CashMargin       |  |
| SecuritiesOrder | Side             |  |
| SecuritiesOrder | SolicitedOrder   |  |
| SecuritiesOrder | CustomerCapacity |  |

| SecuritiesOrder | PositionEffect                    |  |
|-----------------|-----------------------------------|--|
| SecuritiesOrder | ForeignExchangeExecutionRequested |  |
| SecuritiesOrder | SettlementCurrency                |  |
| SecuritiesOrder | OrderOriginatorEligibility        |  |
| SecuritiesOrder | OrderedQuantity                   |  |
| SecuritiesOrder | BusinessProcessType               |  |
| SecuritiesOrder | PlaceOfTrade                      |  |
| SecuritiesOrder | OrderedAmount                     |  |
|                 |                                   |  |

| SecuritiesOrder | GiveUpNumberOfDays            |  |
|-----------------|-------------------------------|--|
| SecuritiesOrder | TradeRegulatoryConditionsType |  |
| SecuritiesOrder | DayOrderQuantity              |  |
| SecuritiesOrder | SecuritiesOrderPartyRole      |  |
| SecuritiesOrder | Status                        |  |
| SecuritiesOrder | RelatedNegotiation            |  |
| SecuritiesOrder | Adjustments                   |  |
| SecuritiesOrder | LegalParameters               |  |
| SecuritiesOrder | OrderPrice                    |  |
| SecuritiesOrder | StopPrice                     |  |

| SecuritiesOrder | SecuritiesOrderAllocation         | Information about the pre<br>Allocation<br>allocation of an order.                                   |
|-----------------|-----------------------------------|------------------------------------------------------------------------------------------------------|
| SecuritiesOrder | OrderExecutionParameters          | Conditions under which a<br>securities order must be<br>SecuritiesOrderParameters<br>executed.       |
| SecuritiesOrder | OrderExecution                    | Result of a securities order.<br>SecuritiesTrade                                                     |
| SecuritiesOrder | OrderingAccount                   | Account impacted by a security<br>SecuritiesAccount<br>transaction.                                  |
| SecuritiesOrder | Quote                             | Quote for which the order<br>SecuritiesQuoteVariable<br>conditions are specified.                    |
| SecuritiesOrder | FundTransactionDirectionIndicator | Indicates the type of investment<br>InvestmentFundTransactionTypeCode<br>funds transaction.          |
| SecuritiesOrder | OrderDate                         | Date/time on which the order<br>was placed by the investor with<br>ISODateTime<br>the trading party. |
| SecuritiesOrder | PegDifference                     | Price difference for a pegged<br>CurrencyAndAmount<br>order.                                         |
| SecuritiesOrder | SecuritiesOrderTradingSession     | Details of a specific trading<br>session associated with a<br>TradingSession<br>securities order.    |
| SecuritiesOrder | RelatedOrderBook                  | Order book whichgenerates an<br>OrderBook<br>order.                                                  |
| SecuritiesOrder | ListTrading                       | List trading information<br>ListTrading<br>containing a serie of orders.                             |
| SecuritiesOrder | BuySideRelatedCrossTrade          | Cross trade for which the buy<br>CrossTrade<br>side information is provided.                         |
| SecuritiesOrder | SellSideRelatedCrossTrade         | Cross trade for which the sell<br>CrossTrade<br>side information is provided.                        |

| SecuritiesOrder | OrderedSecurity           |  |
|-----------------|---------------------------|--|
| SecuritiesOrder | BookingInstructions       |  |
| SecuritiesOrder | ExchangeForPhysicalTrade  |  |
| SecuritiesOrder | QuantityType              |  |
| SecuritiesOrder | ClientOrderIdentification |  |
| SecuritiesOrder | ExecutionInstructions     |  |
| SecuritiesOrder | Type                      |  |
|                 |                           |  |

| SecuritiesOrder                     | LiquidityProvisionActivity |  |
|-------------------------------------|----------------------------|--|
| SecuritiesOrder                     | EventType                  |  |
| SecuritiesOrder                     | PegPrice                   |  |
| SecuritiesOrder                     | LimitPrice                 |  |
| SecuritiesOrderExecutionInstruction |                            |  |
| SecuritiesOrderExecutionInstruction | AllOrNone                  |  |
| SecuritiesOrderExecutionInstruction | CallFirst                  |  |
| SecuritiesOrderExecutionInstruction | Cross                      |  |

| SecuritiesOrderExecutionInstruction | CustomerDisplay         |  |
|-------------------------------------|-------------------------|--|
| SecuritiesOrderExecutionInstruction | Hold                    |  |
| SecuritiesOrderExecutionInstruction | Increase                |  |
| SecuritiesOrderExecutionInstruction | InstitutionsOnly        |  |
| SecuritiesOrderExecutionInstruction | NonNegotiable           |  |
| SecuritiesOrderExecutionInstruction | OverTheDay              |  |
| SecuritiesOrderExecutionInstruction | ParticipateDontInitiate |  |
| SecuritiesOrderExecutionInstruction | PercentOfVolume         |  |

| SecuritiesOrderExecutionInstruction | Scale      |  |
|-------------------------------------|------------|--|
| SecuritiesOrderExecutionInstruction | StayOnSide |  |
| SecuritiesOrderExecutionInstruction | Work       |  |
| SecuritiesOrderExecutionInstruction | GoAlong    |  |
| SecuritiesOrderExecutionInstruction | TryScale   |  |

| SecuritiesOrderExecutionInstruction | DoNotReduce           |  |
|-------------------------------------|-----------------------|--|
| SecuritiesOrderExecutionInstruction | CancelOnSystemFailure |  |
| SecuritiesOrderExecutionInstruction | CancelOnTradingHalt   |  |
| SecuritiesOrderExecutionInstruction | TradeAlong            |  |
| SecuritiesOrderExecutionInstruction | StrictLimit           |  |

| SecuritiesOrderExecutionInstruction | IgnorePriceValidityChecks |  |
|-------------------------------------|---------------------------|--|
| SecuritiesOrderExecutionInstruction | ReinstateOnSystemFailure  |  |
| SecuritiesOrderExecutionInstruction | ReinstateOnTradingHalt    |  |
| SecuritiesOrderExecutionInstruction | CancelIfNotBest           |  |
| SecuritiesOrderExecutionInstruction | ExternalRoutingAllowed    |  |

| SecuritiesOrderExecutionInstruction | ExternalRoutingNotAllowed |  |
|-------------------------------------|---------------------------|--|
| SecuritiesOrderExecutionInstruction | ImbalanceOnly             |  |
| SecuritiesOrderExecutionInstruction | IntermarketSweep          |  |
| SecuritiesOrderExecutionInstruction | Netting                   |  |

| SecuritiesOrderExecutionInstruction | RelatedOrder           |  |
|-------------------------------------|------------------------|--|
| SecuritiesOrderExecutionInstruction | ForeignExchangeNetting |  |
| SecuritiesOrderExecutionInstruction | StrictScale            |  |
| SecuritiesOrderExecutionInstruction | Suspend                |  |
| SecuritiesOrderExecutionInstruction | TryToStop              |  |
| SecuritiesOrderExecutionInstruction | OrderPriceStrategy     |  |
| SecuritiesOrderParameters           |                        |  |
| SecuritiesOrderParameters           | MinimumQuantity        |  |

| SecuritiesOrderParameters | MatchIncrement                  |
|---------------------------|---------------------------------|
| SecuritiesOrderParameters | PegInstructions                 |
| SecuritiesOrderParameters | PreviousClosingPrice            |
| SecuritiesOrderParameters | AutoRouting                     |
| SecuritiesOrderParameters | CorporateActionOptionIndicator  |
| SecuritiesOrderParameters | ExecutionTimeLimit              |
| SecuritiesOrderParameters | PreAllocationConditionIndicator |
| SecuritiesOrderParameters | PriorityIndicator               |
| SecuritiesOrderParameters | RequestedDealCurrency           |
| SecuritiesOrderParameters | OrderHandlingInstruction        |
|                           |                                 |

| SecuritiesOrderParameters | StockLocateRequired   |  |
|---------------------------|-----------------------|--|
| SecuritiesOrderParameters | WorkingIndicator      |  |
| SecuritiesOrderParameters | BookPriorityIndicator |  |
| SecuritiesOrderParameters | MaxPriceLevels        |  |
| SecuritiesOrderParameters | PreTradeAnonymity     |  |
| SecuritiesOrderParameters | GoodTillBooking       |  |

| SecuritiesOrderParameters | ManualOrderIndicator             |        |
|---------------------------|----------------------------------|--------|
| SecuritiesOrderParameters | DirectedOrder                    |        |
| SecuritiesOrderParameters | ReceivedDepartment               |        |
| SecuritiesOrderParameters | CustomerHandlingInstruction      |        |
| SecuritiesOrderParameters | ProcessCode                      |        |
| SecuritiesOrderParameters | RelatedSecuritiesOrder           |        |
| SecuritiesOrderPartyRole  |                                  | Role   |
| SecuritiesOrderPartyRole  | SecuritiesOrder                  |        |
| SecuritiesOrderStatus     |                                  | Status |
| SecuritiesOrderStatus     | ConfirmationRejectedStatusReason |        |
| SecuritiesOrderStatus     | ConfirmationStatus               |        |
|                           |                                  |        |

| CancellationStatus<br>PartiallySettledStatusReason<br>SuspendedStatusReason<br>ListOrderStatus<br>SecuritiesOrder<br>InvestmentFundOrder<br>CumulativeQuantity<br>RemainingQuantity<br>ConditionallyAcceptedStatus<br>OrderStatus<br>AssetPartyRole<br>SecuritiesAccount |                       |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--|
|                                                                                                                                                                                                                                                                          | SecuritiesOrderStatus |  |
|                                                                                                                                                                                                                                                                          | SecuritiesOrderStatus |  |
|                                                                                                                                                                                                                                                                          | SecuritiesOrderStatus |  |
|                                                                                                                                                                                                                                                                          | SecuritiesOrderStatus |  |
|                                                                                                                                                                                                                                                                          | SecuritiesOrderStatus |  |
|                                                                                                                                                                                                                                                                          | SecuritiesOrderStatus |  |
|                                                                                                                                                                                                                                                                          | SecuritiesOrderStatus |  |
|                                                                                                                                                                                                                                                                          | SecuritiesOrderStatus |  |
|                                                                                                                                                                                                                                                                          | SecuritiesOrderStatus |  |
|                                                                                                                                                                                                                                                                          | SecuritiesOrderStatus |  |
|                                                                                                                                                                                                                                                                          | SecuritiesPartyRole   |  |
|                                                                                                                                                                                                                                                                          | SecuritiesPartyRole   |  |

| Unambiguous identification of the<br>cash account used in the context<br>of the securities party role (such<br>SecuritiesPartyRole<br>CashAccount<br>CashAccount<br>as investor cash account used for<br>a corporate action cash<br>distribution)<br>Specifies the security for which<br>SecuritiesPartyRole<br>Security<br>Security<br>the party plays a role.<br>Instructions specific to pegged<br>orders, which consist in an<br>SecuritiesPegOrderInstruction<br>investor buying large amounts of<br>the underlying asset of a<br>derivative it holds.<br>Amount (signed) added to the<br>SecuritiesPegOrderInstruction<br>Offset<br>CurrencyAndAmount<br>peg for a pegged order.<br>SecuritiesPegOrderInstruction<br>PriceType<br>Defines the type of peg.<br>PegTypeCode<br>Describes whether peg is static/<br>SecuritiesPegOrderInstruction<br>MoveType<br>MoveTypeCode<br>fixed or floats.<br>SecuritiesPegOrderInstruction<br>OffsetType<br>Type of peg offset.<br>OffsetTypeCode<br>Specifies nature of resulting<br>SecuritiesPegOrderInstruction<br>LimitType<br>Max35Text<br>pegged price.<br>The scope of "related to" price of<br>SecuritiesPegOrderInstruction<br>Scope<br>the peg (for example, local,<br>PriceProtectionScopeCode<br>global etc).<br>Indicates whether the offset<br>SecuritiesPegOrderInstruction<br>OffsetSign<br>should be added to or subtracted<br>PlusOrMinusIndicator<br>from the peg for a pegged order.<br>SecuritiesPegOrderInstruction<br>Order<br>Order which is pegged.<br>SecuritiesOrderParameters |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |

| SecuritiesPegOrderInstruction | RoundDirection       |
|-------------------------------|----------------------|
| SecuritiesPostTradeBooking    |                      |
| SecuritiesPostTradeBooking    | DayBooking           |
| SecuritiesPostTradeBooking    | BookingUnit          |
| SecuritiesPostTradeBooking    | PreAllocationMethod  |
| SecuritiesPostTradeBooking    | BookingType          |
| SecuritiesPostTradeBooking    | RelatedOrder         |
| SecuritiesPricing             |                      |
| SecuritiesPricing             | PriceMethod          |
| SecuritiesPricing             | PriceType            |
| SecuritiesPricing             | CumDividendIndicator |
| SecuritiesPricing             | CalculationBasis     |
|                               |                      |

| SecuritiesPricing | PriceChangeRelatedStatistics       |
|-------------------|------------------------------------|
| SecuritiesPricing | Rate                               |
| SecuritiesPricing | HighestPriceValueRelatedStatistics |
| SecuritiesPricing | LowestPriceValueRelatedStatistics  |
| SecuritiesPricing | Security                           |
| SecuritiesPricing | SecuritiesTradeExecution           |
| SecuritiesPricing | Yielded                            |
| SecuritiesPricing | TypeOfRate                         |
| SecuritiesPricing | Derivative                         |
| SecuritiesPricing | RelatedWarrant                     |
| SecuritiesPricing | RelatedSecuritiesConversion        |
| SecuritiesPricing | LotBreakdown                       |
| SecuritiesPricing | TypeOfAmount                       |

| SecuritiesPricing | ExercisePriceRelatedEvent                      |  |
|-------------------|------------------------------------------------|--|
| SecuritiesPricing | GenericCashPriceReceivedPerProductRelatedEvent |  |
| SecuritiesPricing | AmountPricePerFinancialInstrumentQuantity      |  |
| SecuritiesPricing | AmountPricePerAmount                           |  |
| SecuritiesPricing | GenericCashPricePaidPerProductRelatedEvent     |  |
| SecuritiesPricing | PriceCalculationPeriod                         |  |
| SecuritiesPricing | CashInLieuOfSharePriceRelatedEvent             |  |
| SecuritiesPricing | OverSubscriptionDepositPriceRelatedEvent       |  |
| SecuritiesPricing | CashValueForTaxRelatedEvent                    |  |
| SecuritiesPricing | MaximumPriceBiddingConditions                  |  |
| SecuritiesPricing | MinimumPriceBiddingConditions                  |  |
|                   |                                                |  |

| SecuritiesPricing | QuotationDate                      |
|-------------------|------------------------------------|
| SecuritiesPricing | YieldCalculation                   |
| SecuritiesPricing | RelatedSecuritiesFinancing         |
| SecuritiesPricing | FundOrderRelatedToExecutedPrice    |
| SecuritiesPricing | FundOrderRelatedToInformativePrice |
| SecuritiesPricing | TaxVoucher                         |
| SecuritiesPricing | SecuritiesTrade                    |
| SecuritiesPricing | NetAssetValueCalculation           |
| SecuritiesPricing | RelatedBuyIn                       |
| SecuritiesPricing | Index                              |
| SecuritiesPricing | InformationPartyRole               |
| SecuritiesPricing | PriceFactPeriod                    |
| SecuritiesPricing | AnalyticsCalculation               |

| SecuritiesPricing | DurationCalculation                             |  |
|-------------------|-------------------------------------------------|--|
| SecuritiesPricing | LifeCalculation                                 |  |
| SecuritiesPricing | Date                                            |  |
| SecuritiesPricing | Spread                                          |  |
| SecuritiesPricing | Order                                           |  |
| SecuritiesPricing | StopPriceOrder                                  |  |
| SecuritiesPricing | Allocation                                      |  |
| SecuritiesPricing | RelatedOrder                                    |  |
| SecuritiesPricing | Issuance                                        |  |
| SecuritiesPricing | Entitlement                                     |  |
| SecuritiesPricing | CashFractionsPriceRelatedSecuritiesDistribution |  |
| SecuritiesPricing | SuscriptionPriceRelatedSecuritiesDistribution   |  |
| SecuritiesPricing | ReinvestmentPriceRelatedSecuritiesDistribution  |  |
|                   |                                                 |  |

| SecuritiesPricing | RelatedFuture                             |  |
|-------------------|-------------------------------------------|--|
| SecuritiesPricing | Distribution                              |  |
| SecuritiesPricing | PriceChangeRedemptionSchedule             |  |
| SecuritiesPricing | RelatedRedemptionSchedule                 |  |
| SecuritiesPricing | PreviousClosingPriceRelatedQuote          |  |
| SecuritiesPricing | RequestedPriceRelatedQuote                |  |
| SecuritiesPricing | PriceRelatedQuote                         |  |
| SecuritiesPricing | MarketPriceRelatedQuote                   |  |
| SecuritiesPricing | Price                                     |  |
| SecuritiesPricing | RelatedCorporateActionPrice               |  |
| SecuritiesPricing | RelatedPosition                           |  |
| SecuritiesPricing | MinimumCashToInstructRelatedEvent         |  |
| SecuritiesPricing | MaximumCashToInstructRelatedEvent         |  |
| SecuritiesPricing | MinimumMultipleCashToInstructRelatedEvent |  |

| SecuritiesProceedsDefinition |                                              | ProceedsDefinition |
|------------------------------|----------------------------------------------|--------------------|
| SecuritiesProceedsDefinition | SecuritiesQuantity                           |                    |
| SecuritiesProceedsDefinition | ConditionalQuantity                          |                    |
| SecuritiesProceedsDefinition | OverAndAboveNormalEnsuredEntitlementQuantity |                    |
| SecuritiesProceedsDefinition | QuantityToReceive                            |                    |
| SecuritiesProceedsDefinition | StatusQuantity                               |                    |
| SecuritiesProceedsDefinition | ParallelTradingPeriod                        |                    |
|                              |                                              |                    |

| SecuritiesProceedsDefinition | AdditionalQuantityForSubscribedResultantSecurities |  |
|------------------------------|----------------------------------------------------|--|
| SecuritiesProceedsDefinition | AdditionalQuantityForExistingSecurities            |  |
| SecuritiesProceedsDefinition | NewToOld                                           |  |
| SecuritiesProceedsDefinition | NewSecuritiesToUnderlyingSecurities                |  |
| SecuritiesProceedsDefinition | ReinvestmentAmount                                 |  |
| SecuritiesProceedsDefinition | IntermediateSecuritiesDistributionType             |  |
| SecuritiesProceedsDefinition | BoardLotSecuritiesQuantity                         |  |

| SecuritiesProceedsDefinition | NewDenominationSecuritiesQuantity       | New denomination of the<br>financial instrument following,<br>SecuritiesQuantity<br>eg, an increase or decrease in<br>nominal value.                                 |
|------------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SecuritiesProceedsDefinition | IntermediateSecuritiesToUnderlyingRatio | Quantity of intermediate<br>securities awarded for a given<br>quantity of underlying security.                                                                       |
| SecuritiesProceedsDefinition | ReinvestmentDiscountToMarket            | Rate of discount for securities<br>purchased through a<br>reinvestment scheme as<br>PercentageRate<br>compared to the current market<br>price of security.           |
| SecuritiesProceedsDefinition | RedemptionDate                          | Date on which the securities will<br>be redeemed (early) for payment<br>ISODateTime<br>of principal.                                                                 |
| SecuritiesProceedsDefinition | AssentedLinePeriod                      | Period during which the assented<br>DateTimePeriod<br>line is available.                                                                                             |
| SecuritiesProceedsDefinition | SellThruIssuerPeriod                    | Period (last day included) during<br>which an account owner can<br>surrender or sell securities to the<br>DateTimePeriod<br>issuer and receive the sale<br>proceeds. |
| SecuritiesProceedsDefinition | ShareRanking                            | Specifies whether the shares are<br>ranking for dividend or pari<br>ShareRankingCode<br>passu.                                                                       |
| SecuritiesQuantity           |                                         | Quantity of a security.                                                                                                                                              |
| SecuritiesQuantity           | Unit                                    | Quantity of a security.<br>DecimalNumber                                                                                                                             |
| SecuritiesQuantity           | SecuritiesTransfer                      | Transfer of a specific quantity of<br>SecuritiesTransfer<br>securities.                                                                                              |
| SecuritiesQuantity           | SecurityIdentification                  | Identifies the security.<br>Security                                                                                                                                 |
|                              |                                         |                                                                                                                                                                      |

| SecuritiesQuantity | Order                                                  |  |
|--------------------|--------------------------------------------------------|--|
| SecuritiesQuantity | Group1Or2Units                                         |  |
| SecuritiesQuantity | RelatedOrderExecution                                  |  |
| SecuritiesQuantity | SecuritiesSettlement                                   |  |
| SecuritiesQuantity | MinimumQuantityDebt                                    |  |
| SecuritiesQuantity | LotBreakdown                                           |  |
| SecuritiesQuantity | MinimumExercisableQuantitySecuritiesConversion         |  |
| SecuritiesQuantity | MinimumExercisableMultipleQuantitySecuritiesConversion |  |
| SecuritiesQuantity | AggregateQuantityBalance                               |  |
| SecuritiesQuantity | SecuritiesProceedsDefinition                           |  |
| SecuritiesQuantity | ConditionalQuantitySecuritiesProceeds                  |  |
|                    |                                                        |  |

| SecuritiesQuantity | OverAndAboveQuantitySecuritiesProceeds         |  |
|--------------------|------------------------------------------------|--|
| SecuritiesQuantity | Entry                                          |  |
| SecuritiesQuantity | Code                                           |  |
| SecuritiesQuantity | ExpectedQuantitySecuritiesProceeds             |  |
| SecuritiesQuantity | StatusRelatedSecuritiesProceeds                |  |
| SecuritiesQuantity | CorporateActionDistribution                    |  |
| SecuritiesQuantity | RelatedEventForFractionalQuantity              |  |
| SecuritiesQuantity | MaximumExercisableQuantitySecuritiesConversion |  |
| SecuritiesQuantity | BoardLotSecuritiesProceeds                     |  |
| SecuritiesQuantity | NewDenominationSecuritiesProceeds              |  |
| SecuritiesQuantity | BackEndOddLotBiddingConditions                 |  |

| SecuritiesQuantity | SecuritiesEntitlement                |  |
|--------------------|--------------------------------------|--|
| SecuritiesQuantity | CorporateActionEvent                 |  |
| SecuritiesQuantity | BiddingConditions                    |  |
| SecuritiesQuantity | Lottery                              |  |
| SecuritiesQuantity | RelatedSubBalance                    |  |
| SecuritiesQuantity | AvailableQuantityBalance             |  |
| SecuritiesQuantity | Trade                                |  |
| SecuritiesQuantity | RatioDenominatorSecuritiesConversion |  |
| SecuritiesQuantity | RatioNumeratorSecuritiesConversion   |  |
| SecuritiesQuantity | MinimumTradedQuantityMarket          |  |
| SecuritiesQuantity | MinimumDenominationDebt              |  |
| SecuritiesQuantity | MinimumIncrementDebt                 |  |
|                    |                                      |  |

| SecuritiesQuantity<br>RelatedOrder<br>SecuritiesQuantity<br>Allocation<br>SecuritiesQuantity<br>Amount<br>SecuritiesQuantity<br>DenominatorRatio<br>SecuritiesQuantity<br>NumeratorRatio<br>SecuritiesQuantity<br>SecuritiesTradeExecution<br>SecuritiesQuantity<br>RelatedCorporateActionEvent<br>SecuritiesQuantity<br>CorporateActionElection<br>SecuritiesQuantity<br>TaxVoucher<br>SecuritiesQuantity<br>RelatedBuyIn |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |  |  |

| SecuritiesQuantity | PreviousDayOrder               |  |
|--------------------|--------------------------------|--|
| SecuritiesQuantity | Liquidity                      |  |
| SecuritiesQuantity | Rate                           |  |
| SecuritiesQuantity | MinimumQuantityOrderParameters |  |
| SecuritiesQuantity | MaximumQuantityRelatedQuote    |  |
| SecuritiesQuantity | UnavailableQuantityBalance     |  |
| SecuritiesQuantity | MatchIncrementOrderParameters  |  |
| SecuritiesQuantity | RelatedIssuance                |  |
| SecuritiesQuantity | Pairoff                        |  |
| SecuritiesQuantity | Issuance                       |  |
|                    |                                |  |

| SecuritiesQuantity | IntermediateToUnderlyingDenominatorDistributionInformation |  |
|--------------------|------------------------------------------------------------|--|
| SecuritiesQuantity | MaximumHoldingDistributionInformation                      |  |
| SecuritiesQuantity | MaximumExercisableQuantityDistributionInformation          |  |
| SecuritiesQuantity | MinimumExercisableQuantityDistributionInformation          |  |
| SecuritiesQuantity | DistributedToUnderlyingDenominatorDistributionInformation  |  |
| SecuritiesQuantity | IntermediateToUnderlyingNumeratorDistributionInformation   |  |
| SecuritiesQuantity | MinimumHoldingDistributionInformation                      |  |
| SecuritiesQuantity | DistributedToUnderlyingNumeratorDistributionInformation    |  |

| SecuritiesQuantity | MaximumHoldingRelatedSecuritiesDistribution                      |  |
|--------------------|------------------------------------------------------------------|--|
| SecuritiesQuantity | IntermediateToUnderlyingNumeratorRelatedSecuritiesDistribution   |  |
| SecuritiesQuantity | IntermediateToUnderlyingDenominatorRelatedSecuritiesDistribution |  |
| SecuritiesQuantity | DistributedToUnderlyingDenominatorRelatedSecuritiesDistribution  |  |
| SecuritiesQuantity | DistributedToUnderlyingNumeratorRelatedSecuritiesDistribution    |  |
| SecuritiesQuantity | MinimumHoldingRelatedSecuritiesDistribution                      |  |
| SecuritiesQuantity | MaximumTradedQuantityMarket                                      |  |
| SecuritiesQuantity | QuantityRelatedQuote                                             |  |
| SecuritiesQuantity | MinimumQuantityRelatedQuote                                      |  |
| SecuritiesQuantity | NetAssetValueCalculation                                         |  |

| SecuritiesQuantity | SidePocket                           |  |
|--------------------|--------------------------------------|--|
| SecuritiesQuantity | Netting                              |  |
| SecuritiesQuantity | RelatedOrderStatus                   |  |
| SecuritiesQuantity | SecuritiesOrderStatus                |  |
| SecuritiesQuantity | RelatedTurnaroundSettlement          |  |
| SecuritiesQuantity | RelatedCashFlow                      |  |
| SecuritiesQuantity | Position                             |  |
| SecuritiesQuantity | MaximumQuantityBiddingConditions     |  |
| SecuritiesQuantity | FrontEndOddLotBiddingConditions      |  |
| SecuritiesQuantity | MinimumQuantityBiddingConditions     |  |
| SecuritiesQuantity | RelatedCorporateActionProtectProcess |  |
| SecuritiesQuantity | DigitalTokenUnit                     |  |

| SecuritiesQuantity<br>PendingQuantity<br>SecuritiesQuantity<br>RejectedQuantity<br>SecuritiesQuoteVariable<br>SecuritiesQuoteVariable<br>Qualifier<br>SecuritiesQuoteVariable<br>Type<br>SecuritiesQuoteVariable<br>QuoteTradingSession<br>SecuritiesQuoteVariable<br>LegSwapType<br>SecuritiesQuoteVariable<br>PriceType<br>SecuritiesQuoteVariable<br>MidSide | SecuritiesQuantity | AcceptedQuantity |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|------------------|--|
|                                                                                                                                                                                                                                                                                                                                                                 |                    |                  |  |
|                                                                                                                                                                                                                                                                                                                                                                 |                    |                  |  |
|                                                                                                                                                                                                                                                                                                                                                                 |                    |                  |  |
|                                                                                                                                                                                                                                                                                                                                                                 |                    |                  |  |
|                                                                                                                                                                                                                                                                                                                                                                 |                    |                  |  |
|                                                                                                                                                                                                                                                                                                                                                                 |                    |                  |  |
|                                                                                                                                                                                                                                                                                                                                                                 |                    |                  |  |
|                                                                                                                                                                                                                                                                                                                                                                 |                    |                  |  |
|                                                                                                                                                                                                                                                                                                                                                                 |                    |                  |  |

| SecuritiesQuoteVariable        | BidSide              |          |
|--------------------------------|----------------------|----------|
| SecuritiesQuoteVariable        | OfferSide            |          |
| SecuritiesQuoteVariable        | RelatedQuote         |          |
| SecuritiesQuoteVariable        | SecuritiesOrder      |          |
| SecuritiesQuoteVariable        | Commission           |          |
| SecuritiesRegistrationDeadline |                      | Deadline |
| SecuritiesRegistrationDeadline | RegistrationDate     |          |
| SecuritiesRegulatoryDetails    |                      |          |
| SecuritiesRegulatoryDetails    | OrderRestrictions    |          |
| SecuritiesRegulatoryDetails    | BrokerSolicitedTrade |          |

| SecuritiesRegulatoryDetails | RelatedOrder         |         |
|-----------------------------|----------------------|---------|
| SecuritiesRelatedFees       |                      | Charges |
| SecuritiesRelatedFees       | Security             |         |
| SecuritiesRelatedFees       | PostageFeeAmount     |         |
| SecuritiesRelatedFees       | RegulatoryFeesAmount |         |
| SecuritiesRelatedFees       | ShippingFeesAmount   |         |
| SecuritiesRelatedFees       | ResearchFee          |         |
| SecuritiesRestriction       |                      |         |
| SecuritiesRestriction       | Security             |         |
| SecuritiesRestriction       | LegalRestrictionType |         |
| SecuritiesRestriction       | Jurisdiction         |         |
|                             |                      |         |

| SecuritiesRestriction | RestrictionType               |            |
|-----------------------|-------------------------------|------------|
| SecuritiesRestriction | InvestorStatusRestrictionType |            |
| SecuritiesRestriction | EffectivePeriod               |            |
| SecuritiesRestriction | Rate                          |            |
| SecuritiesRestriction | InvestorType                  |            |
| SecuritiesSettlement  |                               | Settlement |
| SecuritiesSettlement  | TransferOperation             |            |
| SecuritiesSettlement  | SettlementDate                |            |

| SecuritiesSettlement | PartyRole                      |  |
|----------------------|--------------------------------|--|
| SecuritiesSettlement | SettlementAmount               |  |
| SecuritiesSettlement | HoldingsPlanType               |  |
| SecuritiesSettlement | SecuritiesMovementType         |  |
| SecuritiesSettlement | SettlementQuantity             |  |
| SecuritiesSettlement | SecuritiesTradeExecution       |  |
| SecuritiesSettlement | CurrencyToBuy                  |  |
| SecuritiesSettlement | CurrencyToSell                 |  |
| SecuritiesSettlement | DenominationChoice             |  |
| SecuritiesSettlement | SettlementTransactionCondition |  |

| SecuritiesSettlement<br>BeneficialOwnershipIndicator<br>SecuritiesSettlement<br>MarketClientSide |
|--------------------------------------------------------------------------------------------------|
|                                                                                                  |
|                                                                                                  |
| SecuritiesSettlement<br>Tracking                                                                 |
| SecuritiesSettlement<br>LetterOfGuarantee                                                        |
| SecuritiesSettlement<br>EligibleForCollateral                                                    |
| SecuritiesSettlement<br>AccruedInterestIndicator                                                 |
| SecuritiesSettlement<br>PreConfirmation                                                          |
| SecuritiesSettlement<br>SecuritiesRealTimeGrossSettlement                                        |
| SecuritiesSettlement<br>BlockTrade                                                               |

| SecuritiesSettlement | SettlementSystemMethod          | Specifies whether the settlement<br>instruction is to be settled<br>through the default or the<br>alternate settlement system.     | SettlementSystemMethodCode |                                         |
|----------------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------|----------------------------|-----------------------------------------|
| SecuritiesSettlement | AutomaticBorrowing              | Condition for automatic<br>borrowing.                                                                                              | AutoBorrowingCode          |                                         |
| SecuritiesSettlement | PartialSettlementIndicator      | Specifies whether partial<br>settlement is allowed.                                                                                | YesNoIndicator             |                                         |
| SecuritiesSettlement | HoldIndicator                   | Specifies whether the transaction<br>is on hold/blocked/frozen.                                                                    | YesNoIndicator             |                                         |
| SecuritiesSettlement | RequestedSafekeepingPlace       | Place requested as the place of<br>safekeeping.                                                                                    | SafekeepingPlace           | SecuritiesSettlement                    |
| SecuritiesSettlement | PairOff                         | Buy and sell trades are settled in<br>cash, based on the difference in<br>PairOff<br>the prices between the off<br>setting trades. |                            | RelatedSecuritiesSettlement             |
| SecuritiesSettlement | AccruedInterest                 | Interest included in the<br>Interest<br>settlement.                                                                                |                            | SecuritiesSettlement                    |
| SecuritiesSettlement | SecuritiesClearing              | Clearing process which triggers<br>the settlement process.                                                                         | SecuritiesClearing         | SecuritiesSettlement                    |
| SecuritiesSettlement | Payment                         | Specifies the cash payment<br>information of a securities<br>Payment<br>settlement.                                                |                            | RelatedSecuritiesSettlement             |
| SecuritiesSettlement | SettledAllocation               | Allocation which is settled.<br>Allocation                                                                                         |                            | SettlementExecutionParameters           |
| SecuritiesSettlement | RelatedForeignExchangeOperation | Entry details related to currency<br>exchange information.                                                                         | ForeignExchangeTrade       | CurrencyExchangeForSecuritiesSettlement |
| SecuritiesSettlement | Security                        | Security which is settled.<br>Security                                                                                             |                            | SecuritiesSettlement                    |

| SecuritiesSettlement<br>Position<br>SecuritiesSettlement<br>Rollover<br>SecuritiesSettlement<br>TurnedQuantity<br>SecuritiesSettlement<br>SettlementReason<br>SecuritiesSettlement<br>SettlementType<br>SecuritiesSettlement<br>BuyInState<br>SecuritiesSettlement<br>BuyInDeferral<br>SecuritiesSettlement<br>CashCompensationAmount<br>SecuritiesSettlement<br>ForfeitureOfInterestIndicator<br>SecuritiesSettlementPartyRole<br>SettlementPartyRole |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |

| SecuritiesSettlementPartyRole | SecuritiesSettlement       |        |
|-------------------------------|----------------------------|--------|
| SecuritiesSettlementPartyRole | SecuritiesSettlementSystem |        |
| SecuritiesSettlementPartyRole | SettlingCapacity           |        |
| SecuritiesSettlementPartyRole | TaxCapacity                |        |
| SecuritiesSettlementSystem    |                            | System |
| SecuritiesSettlementSystem    | SettlementParty            |        |
| SecuritiesStatus              |                            | Status |
| SecuritiesStatus              | PaymentStatus              |        |
| SecuritiesStatus              | Status                     |        |
| SecuritiesStatus              | RegistrationStatus         |        |
| SecuritiesStatus              | Security                   |        |
| SecuritiesSwapLeg             |                            |        |

| SecuritiesSwapLeg | Amount              |     |
|-------------------|---------------------|-----|
| SecuritiesSwapLeg | Benchmark           |     |
| SecuritiesSwapLeg | CurvePoint          |     |
| SecuritiesSwapLeg | BenchmarkYield      |     |
| SecuritiesSwapLeg | BenchmarkOffset     |     |
| SecuritiesSwapLeg | SpotSellSwap        |     |
| SecuritiesSwapLeg | SpotBuySwap         |     |
| SecuritiesSwapLeg | ForwardBuyBackSwap  |     |
| SecuritiesSwapLeg | ForwardSellBackSwap |     |
| SecuritiesTax     |                     | Tax |

| SecuritiesTax | TaxableIncomePerShare           |  |
|---------------|---------------------------------|--|
| SecuritiesTax | TaxableIncomePerShareCalculated |  |
| SecuritiesTax | EUCapitalGain                   |  |
| SecuritiesTax | EUDividendStatus                |  |
| SecuritiesTax | TaxableIncomePerDividend        |  |

| SecuritiesTax | StampDutyType                 |  |
|---------------|-------------------------------|--|
| SecuritiesTax | StampDutyTaxBasis             |  |
| SecuritiesTax | TaxVoucher                    |  |
| SecuritiesTax | TaxableIncomePerDividendShare |  |
| SecuritiesTax | RelatedTax                    |  |
| SecuritiesTax | TaxLotNumber                  |  |
| SecuritiesTax | Security                      |  |
| SecuritiesTax | TaxRuleExemptIndicator        |  |
| SecuritiesTax | EffectivePeriod               |  |
| SecuritiesTax | FrankedRate                   |  |
| SecuritiesTax | TEFRARule                     |  |

| SecuritiesTax   | Jurisdiction                          |       |
|-----------------|---------------------------------------|-------|
| SecuritiesTrade |                                       | Trade |
| SecuritiesTrade | SecuritiesTradeRelatedIdentifications |       |
| SecuritiesTrade | TradeAmount                           |       |
| SecuritiesTrade | OpeningClosingIndicator               |       |
| SecuritiesTrade | TradeTransactionCondition             |       |
| SecuritiesTrade | SecuritiesTradeStatus                 |       |
| SecuritiesTrade | Activity                              |       |
| SecuritiesTrade | TradeQuantity                         |       |

| SecuritiesTrade | TradeOriginationDate           |  |
|-----------------|--------------------------------|--|
| SecuritiesTrade | ClearingFeeType                |  |
| SecuritiesTrade | Security                       |  |
| SecuritiesTrade | TradePrice                     |  |
| SecuritiesTrade | PartyRole                      |  |
| SecuritiesTrade | SecuritiesFinancingClosingData |  |
| SecuritiesTrade | TradingExecution               |  |
| SecuritiesTrade | TradeAllocation                |  |
| SecuritiesTrade | RelatedOrder                   |  |
| SecuritiesTrade | SecuritiesFinancingOpeningData |  |
| SecuritiesTrade | TransactionType                |  |

| SecuritiesTrade          | LegalFramework            |
|--------------------------|---------------------------|
| SecuritiesTrade          | SecuritiesTransactionType |
| SecuritiesTradeExecution |                           |
| SecuritiesTradeExecution | StampDutyIndicator        |
| SecuritiesTradeExecution | ProcessingPosition        |
| SecuritiesTradeExecution | SecuritiesSettlement      |
| SecuritiesTradeExecution | DealPrice                 |

| SecuritiesTradeExecution<br>MarginAmount<br>SecuritiesTradeExecution<br>ExecutedTradeQuantity<br>SecuritiesTradeExecution<br>OffMarketReason<br>SecuritiesTradeExecution<br>RelatedTrade<br>SecuritiesTradeExecution<br>DealExecutionAmount<br>SecuritiesTradeExecution<br>PaymentObligation<br>SecuritiesTradeExecution<br>SecuritiesDeliveryObligation<br>SecuritiesTradeExecution<br>ReportingType<br>SecuritiesTradeIdentification<br>TradeIdentification<br>SecuritiesTradeIdentification<br>IdentifiedTrade |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |

| SecuritiesTradeIdentification | MarketInfrastructureTransactionIdentification     |  |
|-------------------------------|---------------------------------------------------|--|
| SecuritiesTradeIdentification | ProcessorTransactionIdentification                |  |
| SecuritiesTradeIdentification | PoolIdentification                                |  |
| SecuritiesTradeIdentification | CollateralTransactionIdentification               |  |
| SecuritiesTradeIdentification | ClientTripartyCollateralTransactionIdentification |  |
| SecuritiesTradeIdentification | TripartyAgentCollateralTransactionIdentification  |  |
| SecuritiesTradeIdentification | BasketIdentification                              |  |
| SecuritiesTradeIdentification | ProgramIdentification                             |  |
| SecuritiesTradeIdentification | BlockIdentification                               |  |
|                               |                                                   |  |

| SecuritiesTradeIdentification<br>ComplianceIdentification<br>SecuritiesTradeIdentification<br>CSDTransactionIdentification<br>SecuritiesTradeIdentification<br>CentralCounterpartyTransactionIdentification<br>SecuritiesTradeIdentification<br>CancellationRequestIdentification<br>SecuritiesTradeIdentification<br>CounterpartyMarketInfrastructureTransactionIdentification<br>SecuritiesTradePartyRole<br>TradePartyRole<br>SecuritiesTradePartyRole<br>SecuritiesTrade<br>SecuritiesTradeStatus<br>Status<br>SecuritiesTradeStatus<br>MatchingStatus<br>SecuritiesTradeStatus<br>AffirmationStatus | SecuritiesTradeIdentification | AllocationIdentification |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                               |                          |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                               |                          |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                               |                          |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                               |                          |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                               |                          |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                               |                          |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                               |                          |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                               |                          |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                               |                          |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                               |                          |  |

| SecuritiesTradeStatus | Reason                                |  |
|-----------------------|---------------------------------------|--|
| SecuritiesTradeStatus | SecuritiesTrade                       |  |
| SecuritiesTradeStatus | TransactionStatus                     |  |
| SecuritiesTradeStatus | ReplacementProcessingStatus           |  |
| SecuritiesTradeStatus | CancellationStatus                    |  |
| SecuritiesTradeStatus | CancellationRight                     |  |
| SecuritiesTradeStatus | TransferStatus                        |  |
| SecuritiesTradeStatus | AllegedStatus                         |  |
| SecuritiesTradeStatus | CollateralAllocationStatus            |  |
| SecuritiesTradeStatus | RepoCallRequestStatus                 |  |
| SecuritiesTradeStatus | SettlementConditionModificationStatus |  |
|                       |                                       |  |

| SecuritiesTradeStatus       | MatchingProcess               |              |
|-----------------------------|-------------------------------|--------------|
| SecuritiesTradeStatus       | RelatedSecuritiesTransfer     |              |
| SecuritiesTradeStatus       | TradeConfirmationStatus       |              |
| SecuritiesTradeStatusReason |                               | StatusReason |
| SecuritiesTradeStatusReason | UnmatchedReason               |              |
| SecuritiesTradeStatusReason | DeniedReason                  |              |
| SecuritiesTradeStatusReason | SecuritiesTradeStatus         |              |
| SecuritiesTradeStatusReason | GeneratedReason               |              |
| SecuritiesTradeStatusReason | AllegementReason              |              |
| SecuritiesTradeStatusReason | PendingSettlementReason       |              |
| SecuritiesTradeStatusReason | RepoCallAcknowledgementReason |              |
| SecuritiesTradeStatusReason | RepairReason                  |              |
|                             |                               |              |

| SecuritiesTradeStatusReason | DeliveryReturnReason     |                          |
|-----------------------------|--------------------------|--------------------------|
| SecuritiesTradeStatusReason | CounterpartyStatusReason |                          |
| SecuritiesTradeStatusReason | ModifiedStatusReason     |                          |
| SecuritiesTradeSystemRole   |                          | SecuritiesTradePartyRole |
| SecuritiesTransaction       |                          | SecuritiesTrade          |
| SecuritiesTransaction       | ReplacedAmount           |                          |
| SecuritiesTransfer          |                          | ObligationFulfilment     |
| SecuritiesTransfer          | Identification           |                          |
| SecuritiesTransfer          | TransferredQuantity      |                          |
| SecuritiesTransfer          | Account                  |                          |
| SecuritiesTransfer          | TransferType             |                          |

| SecuritiesTransfer | RelatedSettlement            | Settlement process which is the<br>SecuritiesSettlement<br>source of the transfer operation.                                                                                 |  |
|--------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| SecuritiesTransfer | OwnAccountTransferIndicator  | Indicates whether the transfer<br>results in a change of beneficial<br>YesNoIndicator<br>owner.                                                                              |  |
| SecuritiesTransfer | PhysicalDelivery             | Information related to physical<br>PhysicalDelivery<br>delivery of the securities.                                                                                           |  |
| SecuritiesTransfer | LateDeliveryDate             | Date and time after the<br>settlement date specified in the<br>trade, used for pool trades<br>ISODateTime<br>resulting from the original To Be<br>Assigned (TBA) securities. |  |
| SecuritiesTransfer | TransferTax                  | Tax related to the transfer of a<br>Tax<br>financial instrument.                                                                                                             |  |
| SecuritiesTransfer | TransferReason               | Identifies the transfer reason.<br>TransferReasonCode                                                                                                                        |  |
| SecuritiesTransfer | PartialSettlementType        | Information about partial<br>PartialSettlementV2Code<br>settlement.                                                                                                          |  |
| SecuritiesTransfer | SecuritiesDeliveryObligation | Obligation for one party to<br>deliver securities to another<br>SecuritiesDeliveryObligation<br>party.                                                                       |  |
| SecuritiesTransfer | BookEntry                    | Record in a securities account<br>resulting from the transfer of a<br>SecuritiesEntry<br>security.                                                                           |  |
| SecuritiesTransfer | TransactionIdentification    | Unambiguous identification of a<br>Max35Text<br>securities transfer.                                                                                                         |  |
| SecuritiesTransfer | Security                     | Security which is transferred.<br>Security                                                                                                                                   |  |
| SecuritiesTransfer | Status                       | Status of a securities transfer.<br>SecuritiesTradeStatus                                                                                                                    |  |

| Security |                               | Asset |
|----------|-------------------------------|-------|
| Security | Identification                |       |
| Security | RegisteredDistributionCountry |       |
| Security | DenominationCurrency          |       |
| Security | RegistrationForm              |       |
| Security | DematerialisedIndicator       |       |
| Security | EUSavingsDirective            |       |
| Security | SecuritiesQuantity            |       |
| Security | Fees                          |       |
| Security | Pricing                       |       |
| Security | SecuritiesAccount             |       |
| Security | TradingMarket                 |       |

| Security | PlaceOfListing                        |  |
|----------|---------------------------------------|--|
| Security | Registration                          |  |
| Security | Restriction                           |  |
| Security | CorporateEvent                        |  |
| Security | TemporaryFinancialInstrumentIndicator |  |
| Security | AvailableDate                         |  |
| Security | DeclarationDetails                    |  |
| Security | Spread                                |  |
| Security | Dividend                              |  |
| Security | Balance                               |  |
| Security | FungibleIndicator                     |  |
| Security | Appearance                            |  |

| Security | NearTermPositionLimit          | Position limit in the near-term<br>contract for a given exchange<br>Number<br>traded product.                                                          |
|----------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Security | ContractSettlementMonth        | Specifies when the contract (i.e.<br>ISOYearMonth<br>MBS/TBA) will settle.                                                                             |
| Security | MinimumTradingPricingIncrement | Minimum price increase for a<br>given exchange-traded<br>Number<br>Instrument                                                                          |
| Security | Rating                         | Rating(s) of the security.<br>Rating                                                                                                                   |
| Security | CouponAttached                 | Coupon information of the<br>CouponAttached<br>security.                                                                                               |
| Security | Sector                         | Indicates the market sector the<br>security is classified as<br>Sector<br>pharmaceuticals, automobile,<br>housing, etc.                                |
| Security | WarrantAttachedOnDelivery      | Indicates whether the warrants<br>on a financial instrument (which<br>YesNoIndicator<br>has been traded cum warrants)<br>will be attached on delivery. |
| Security | StrippableIndicator            | Indicates whether the interest is<br>YesNoIndicator<br>separable from the principal.                                                                   |
| Security | FirstDealingDate               | Date on which new securities<br>ISODateTime<br>begin trading.                                                                                          |
| Security | TaxDetails                     | Tax details of the security.<br>SecuritiesTax                                                                                                          |
| Security | SecuritiesTrade                | Trade in which the security is<br>SecuritiesTrade<br>involved.                                                                                         |

| Security | RegistrationJurisdiction            |  |
|----------|-------------------------------------|--|
| Security | PartyRole                           |  |
| Security | SecurityStatus                      |  |
| Security | Modification                        |  |
| Security | RedemptionSchedule                  |  |
| Security | SecuritiesSettlement                |  |
| Security | SecuritiesTransfer                  |  |
| Security | CorporateActionStandingInstructions |  |
| Security | Quote                               |  |
| Security | SecuritiesOrder                     |  |
| Security | RelatedVariableInterest             |  |
|          |                                     |  |

| Security<br>Conversion<br>Security<br>ComponentSecurity<br>Security<br>RecompositionIndicator<br>Security<br>Series<br>Security<br>PercentageOfDebtClaim<br>Security<br>CoverRate<br>Security<br>MaturityRedemption<br>Security<br>RelatedMarginCall<br>Security<br>CloseLink |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                               |  |  |

| Security                      | PotentialEuroSystemEligibility |                              |
|-------------------------------|--------------------------------|------------------------------|
| Security                      | MinimumQuantity                |                              |
| Security                      | RestrictedIndicator            |                              |
| SecurityCertificate           |                                | Document                     |
| SecurityCertificate           | ElectronicSignature            |                              |
| SecurityCertificate           | SecurityCertificatePartyRole   |                              |
| SecurityCertificate           | NetworkAccess                  |                              |
| SecurityCertificate           | CertificateType                |                              |
| SecurityCertificateHolderRole |                                | SecurityCertificatePartyRole |
| SecurityCertificateIssuerRole |                                | SecurityCertificatePartyRole |
| SecurityCertificatePartyRole  |                                | Role                         |
| SecurityCertificatePartyRole  | SecurityCertificate            |                              |
|                               |                                |                              |

| SellerBank   |                   | TradePartyRole |
|--------------|-------------------|----------------|
| SellerRole   |                   | TradePartyRole |
| Service      |                   | Product        |
| Service      | Amount            |                |
| Service      | Type              |                |
| Service      | TaxDesignation    |                |
| Service      | Rate              |                |
| ServiceLevel |                   |                |
| ServiceLevel | PaymentProcessing |                |
| ServiceLevel | Code              |                |
| ServiceLevel | Other             |                |
| ServiceLevel | Bilateral         |                |

| ServicingPartyRole              |                                         | CollateralPartyRole                |
|---------------------------------|-----------------------------------------|------------------------------------|
| Settlement                      |                                         |                                    |
| Settlement                      | CentralCounterpartyEligibilityIndicator |                                    |
| Settlement                      | StandingSettlementInstruction           |                                    |
| Settlement                      | SettlementPartyRole                     |                                    |
| Settlement                      | Trade                                   |                                    |
| SettlementInstructionSystemRole |                                         | CashSettlementInstructionPartyRole |
| SettlementInstructionSystemRole | System                                  |                                    |
| SettlementPartyRole             |                                         | Role                               |
| SettlementPartyRole             | SettlementAccount                       |                                    |
| SettlementPartyRole             | Settlement                              |                                    |
|                                 |                                         |                                    |

| SettlementTimeRequest |                |                          |
|-----------------------|----------------|--------------------------|
| SettlementTimeRequest | Payment        |                          |
| SettlementTimeRequest | CLSTime        |                          |
| SettlementTimeRequest | TillTime       |                          |
| SettlementTimeRequest | FromTime       |                          |
| SettlementTimeRequest | RejectTime     |                          |
| Settlor               |                | InvestmentFundPartyRole  |
| ShareholderRegister   |                |                          |
| ShareholderRegister   | Identification |                          |
| ShareholderRegister   | Entry          |                          |
| ShipFrom              |                | CommercialTradePartyRole |

| ShipTo            |                              | CommercialTradePartyRole |
|-------------------|------------------------------|--------------------------|
| ShipmentDateRange |                              |                          |
| ShipmentDateRange | LatestShipmentDate           |                          |
| ShipmentDateRange | RelatedTransport             |                          |
| ShipmentDateRange | EarliestShipmentDate         |                          |
| ShipmentDateRange | ShipmentDate                 |                          |
| SidePocket        |                              |                          |
| SidePocket        | SidePocketInclusionIndicator |                          |
| SidePocket        | SidePocketIdentification     |                          |

| SidePocket         | InvestmentAccount       |          |
|--------------------|-------------------------|----------|
| SidePocket         | SidePocketQuantity      |          |
| Signature          |                         | Evidence |
| Signature          | Conditions              |          |
| Signature          | CardPaymentValidation   |          |
| SignatureCondition |                         |          |
| SignatureCondition | RequiredSignatureNumber |          |
| SignatureCondition | SignatoryRightIndicator |          |
| SignatureCondition | Mandate                 |          |
| SignatureCondition | SignatureOrderIndicator |          |

| SignatureCondition | SignatureOrder       |                          |
|--------------------|----------------------|--------------------------|
| SignatureCondition | Signature            |                          |
| SourceOfPrice      |                      | InformationPartyRole     |
| SourceOfPrice      | MarketIdentification |                          |
| SourceOfPrice      | Type                 |                          |
| Sponsor            |                      | SecuritiesPartyRole      |
| SponsoringFirm     |                      | SecuritiesOrderPartyRole |
| Spread             |                      |                          |
| Spread             | BenchmarkSecurity    |                          |
| Spread             | SecuritiesFinancing  |                          |

| Spread | SpreadRate                  |  |
|--------|-----------------------------|--|
| Spread | BasisPointSpread            |  |
| Spread | Index                       |  |
| Spread | BenchmarkPrice              |  |
| Spread | RelatedIndicationOfInterest |  |
| Spread | IndicationOfInterest        |  |
| Spread | RelatedInterest             |  |
| Spread | BenchmarkCurve              |  |
| Spread | PriceOffset                 |  |

| StandingOrder                          |  |
|----------------------------------------|--|
| StandingOrder<br>Identification        |  |
| StandingOrder<br>Type                  |  |
| StandingOrder<br>ValidityPeriod        |  |
| StandingOrder<br>LinkSetIdentification |  |
| StandingOrder<br>StandingOrderSequence |  |
| StandingOrder<br>Amount                |  |
| StandingOrder<br>CreditAccount         |  |
| StandingOrder<br>DebitAccount          |  |

| StandingOrder                 | Frequency                 |                             |
|-------------------------------|---------------------------|-----------------------------|
| StandingOrder                 | EventDescription          |                             |
| StandingOrder                 | Day                       |                             |
| StandingOrder                 | TimeSpecification         |                             |
| StandingOrder                 | PaymentInstructionTrigger |                             |
| StandingOrder                 | IncludedStandingOrder     |                             |
| StandingOrder                 | LinkSet                   |                             |
| StandingOrderResponsible      |                           | AccountResponsiblePartyRole |
| StandingSettlementInstruction |                           |                             |
| StandingSettlementInstruction | Settlement                |                             |
| StandingSettlementInstruction | FXStandingInstruction     |                             |

| StandingSettlementInstruction | SettlementStandingInstructionDatabase |  |
|-------------------------------|---------------------------------------|--|
| StandingSettlementInstruction | Identification                        |  |
| StandingSettlementInstruction | RelatedCollateralAgreement            |  |
| StandingSettlementInstruction | SSIDatabaseName                       |  |
| StandingSettlementInstruction | SSIDatabaseProvider                   |  |
| StandingSettlementInstruction | ValidityPeriod                        |  |
| StandingSettlementInstruction | Currency                              |  |
| StandingSettlementInstruction | Asset                                 |  |
| Status                        |                                       |  |
| Status                        | StatusReason                          |  |
| Status                        | StatusDateTime                        |  |
|                               |                                       |  |

| Status           | ValidityTime                 |                        |
|------------------|------------------------------|------------------------|
| Status           | StatusDescription            |                        |
| Status           | InstructionProcessingStatus  |                        |
| Status           | PartyRole                    |                        |
| Status           | SettlementStatus             |                        |
| Status           | CancellationProcessingStatus |                        |
| Status           | TransactionProcessingStatus  |                        |
| Status           | ModificationProcessingStatus |                        |
| StatusOriginator |                              | InvestigationPartyRole |
| StatusReason     |                              |                        |
| StatusReason     | Status                       |                        |
| StatusReason     | Reason                       |                        |
| StatusReason     | NoSpecifiedReason            |                        |
|                  |                              |                        |

| StatusReason  | DataSourceScheme           |                |
|---------------|----------------------------|----------------|
| StatusReason  | RejectedStatusReason       |                |
| StatusReason  | FailingReason              |                |
| StatusReason  | CancellationReason         |                |
| StatusReason  | PendingReason              |                |
| StatusReason  | RejectionReason            |                |
| StatusReason  | AcknowledgedAcceptedReason |                |
| StatusReason  | RelatedClosureReason       |                |
| StepInBroker  |                            | Broker         |
| StepOutBroker |                            | Broker         |
| StockExchange |                            | TradePartyRole |
| StockExchange | Market                     |                |
|               |                            |                |

| SubmittingPartyRole   |                      | SystemPartyRole              |
|-----------------------|----------------------|------------------------------|
| SubscriptionExecution |                      | InvestmentFundOrderExecution |
| SubscriptionExecution | EquityComponent      |                              |
| SubscriptionExecution | CashComponent        |                              |
| SubscriptionExecution | InvestedNetAmount    |                              |
| SubscriptionExecution | Refund               |                              |
| SubscriptionExecution | SubscriptionInterest |                              |
| SubscriptionExecution | TaxEfficientProduct  |                              |
| SubscriptionOrder     |                      | InvestmentFundOrder          |
| SuccessorOnDeath      |                      | InvestmentAccountPartyRole   |
|                       |                      |                              |

| SuspensionPeriod |                                                |  |
|------------------|------------------------------------------------|--|
| SuspensionPeriod | PrivilegeSuspensionPeriod                      |  |
| SuspensionPeriod | DepositorySuspensionPeriodForWithdrawal        |  |
| SuspensionPeriod | DepositorySuspensionPeriodForBookEntryTransfer |  |
| SuspensionPeriod | DepositorySuspensionPeriodForDepositAtAgent    |  |

| SuspensionPeriod | DepositorySuspensionPeriodForDeposit                 |  |
|------------------|------------------------------------------------------|--|
| SuspensionPeriod | DepositorySuspensionPeriodForPledge                  |  |
| SuspensionPeriod | DepositorySuspensionPeriodForSegregation             |  |
| SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalAtAgent       |  |
| SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalInNomineeName |  |

| SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalInStreetName |                              |
|------------------|-----------------------------------------------------|------------------------------|
| SuspensionPeriod | CoDepositoriesSuspensionPeriod                      |                              |
| SuspensionPeriod | CorporateActionEvent                                |                              |
| Swaps            |                                                     | Derivative                   |
| Swaps            | SovereignIssuer                                     |                              |
| Swaps            | Obligation                                          |                              |
| SwitchExecution  |                                                     | InvestmentFundOrderExecution |
| SwitchExecution  | RedemptionLeg                                       |                              |
| SwitchExecution  | SubscriptionLeg                                     |                              |
|                  |                                                     |                              |

| SwitchExecutionRedemptionLeg   |                                     | RedemptionExecution   |
|--------------------------------|-------------------------------------|-----------------------|
| SwitchExecutionRedemptionLeg   | RelatedSwitchExecution              |                       |
| SwitchExecutionRedemptionLeg   | PercentageOfTotalSubscriptionAmount |                       |
| SwitchExecutionSubscriptionLeg |                                     | SubscriptionExecution |
| SwitchExecutionSubscriptionLeg | RelatedSwitchExecution              |                       |
| SwitchExecutionSubscriptionLeg | PercentageOfTotalRedemptionAmount   |                       |
| SwitchOrder                    |                                     | InvestmentFundOrder   |
| SwitchOrder                    | AdditionalCashIn                    |                       |

| SwitchOrder           | ResultingCashOut                    |                   |
|-----------------------|-------------------------------------|-------------------|
| SwitchOrder           | TotalRedemptionAmount               |                   |
| SwitchOrder           | TotalSubscriptionAmount             |                   |
| SwitchOrder           | RedemptionLeg                       |                   |
| SwitchOrder           | SubscriptionLeg                     |                   |
| SwitchRedemptionLeg   |                                     | RedemptionOrder   |
| SwitchRedemptionLeg   | RedemptionRelatedSwitchOrder        |                   |
| SwitchRedemptionLeg   | PercentageOfTotalSubscriptionAmount |                   |
| SwitchSubscriptionLeg |                                     | SubscriptionOrder |
| SwitchSubscriptionLeg | SubscriptionRelatedSwitchOrder      |                   |
|                       |                                     |                   |

| SwitchSubscriptionLeg | PercentageOfTotalRedemptionAmount |            |
|-----------------------|-----------------------------------|------------|
| System                |                                   | RolePlayer |
| System                | SystemIdentification              |            |
| System                | Location                          |            |
| System                | Reconciliation                    |            |
| System                | Availability                      |            |
| System                | Event                             |            |
| System                | PartyRole                         |            |
| System                | Status                            |            |

| System                  | SystemGeneratedInformation |                 |
|-------------------------|----------------------------|-----------------|
| System                  | VersionValidityPeriod      |                 |
| System                  | SystemDateTime             |                 |
| System                  | Negotiation                |                 |
| System                  | Account                    |                 |
| System                  | Trade                      |                 |
| System                  | Assessment                 |                 |
| System                  | TradesPosition             |                 |
| System                  | SystemLanguage             |                 |
| SystemAdministratorRole |                            | SystemPartyRole |
| SystemAvailability      |                            |                 |
| SystemAvailability      | AvailableSessionPeriod     |                 |
| SystemAvailability      | System                     |                 |

| SystemAvailability<br>ClosureInformation    |
|---------------------------------------------|
| SystemAvailability<br>Date                  |
| SystemAvailability<br>ClosurePeriod         |
| SystemBusinessInformation                   |
| SystemBusinessInformation<br>Qualifier      |
| SystemBusinessInformation<br>Subject        |
| SystemBusinessInformation<br>SubjectDetails |
| SystemBusinessInformation<br>Identification |
| SystemBusinessInformation<br>Reference      |
| SystemBusinessInformation<br>System         |

| SystemClosureInformation |                         |
|--------------------------|-------------------------|
| SystemClosureInformation | Period                  |
| SystemClosureInformation | SystemAvailability      |
| SystemClosureInformation | ClosureReason           |
|                          |                         |
| SystemEventInformation   |                         |
|                          |                         |
| SystemEventInformation   | Type                    |
| SystemEventInformation   | Time                    |
| SystemEventInformation   | System                  |
| SystemIdentification     |                         |
| SystemIdentification     | IdentificationForSystem |
| SystemIdentification     | Model                   |
| SystemIdentification     | SerialNumber            |
|                          |                         |

| SystemIdentification | ApprovalNumber |                 |
|----------------------|----------------|-----------------|
| SystemIdentification | SystemVersion  |                 |
| SystemIdentification | SystemName     |                 |
| SystemIdentification | Identification |                 |
| SystemMemberRole     |                | SystemPartyRole |
| SystemMemberRole     | CashBalance    |                 |
| SystemMemberRole     | Type           |                 |
|                      | MemberStatus   |                 |

| SystemMemberRole               | Limit                |                 |
|--------------------------------|----------------------|-----------------|
| SystemMemberRole               | Account              |                 |
| SystemName                     |                      |                 |
| SystemName                     | Name                 |                 |
| SystemName                     | SystemIdentification |                 |
| SystemPartyRole                |                      | Role            |
| SystemPartyRole                | RelatedSystem        |                 |
| SystemReferenceDataResponsible |                      | SystemPartyRole |
|                                |                      |                 |

| SystemStatus           |                  | Status                   |
|------------------------|------------------|--------------------------|
| SystemStatus           | Status           |                          |
| SystemStatus           | MemberStatus     |                          |
| SystemStatus           | System           |                          |
| SystemStatus           | SystemMemberRole |                          |
| SystematicInternaliser |                  | SecuritiesTradePartyRole |
| TakerRole              |                  | CollateralPartyRole      |
| Tax                    |                  |                          |
| Tax                    | ExemptionReason  |                          |
| Tax                    | Country          |                          |
|                        |                  |                          |

| Tax | TaxLiabilityValueCalculation |  |
|-----|------------------------------|--|
| Tax | Type                         |  |
| Tax | Amount                       |  |
| Tax | Rate                         |  |
| Tax | TaxableParty                 |  |
| Tax | TaxRefundValueCalculation    |  |
| Tax | Basis                        |  |
| Tax | SecuritiesTransfer           |  |
| Tax | TaxRateType                  |  |
| Tax | TaxAccount                   |  |
| Tax | TaxationConditions           |  |
| Tax | Adjustment                   |  |
| Tax | Interest                     |  |

| Tax | Identification            |  |
|-----|---------------------------|--|
| Tax | RelatedPaymentSettlement  |  |
| Tax | TaxableBaseAmount         |  |
| Tax | TaxDate                   |  |
| Tax | CertificateIdentification |  |
| Tax | AdministrationZone        |  |
| Tax | Method                    |  |
| Tax | Record                    |  |
| Tax | Product                   |  |
| Tax | CurrencyExchange          |  |
| Tax | Currency                  |  |
| Tax | PartyRole                 |  |
| Tax | TaxDeduction              |  |

| Tax                 | RelatedCorporateActionDistribution |  |
|---------------------|------------------------------------|--|
| Tax                 | CalculationDate                    |  |
| Tax                 | Dividend                           |  |
| Tax                 | WithholdingTaxType                 |  |
| Tax                 | CorporateActionEvent               |  |
| Tax                 | TaxIdentificationType              |  |
| Tax                 | TaxRateMarker                      |  |
| TaxEfficientProduct |                                    |  |
| TaxEfficientProduct | EstimatedValue                     |  |
| TaxEfficientProduct | PreviousYears                      |  |
| TaxEfficientProduct | CurrentInvestmentAmount            |  |
| TaxEfficientProduct | Amount                             |  |
| TaxEfficientProduct | UnusedTaxDeduction                 |  |
| TaxEfficientProduct | TaxCalculationBase                 |  |
|                     |                                    |  |

| TaxEfficientProduct<br>InvestorTaxReference<br>TaxEfficientProduct<br>RelatedInvestmentPlan<br>TaxEfficientProduct<br>TaxEfficientProductType<br>TaxEfficientProduct<br>AmountType<br>TaxEfficientProduct<br>InvestmentsToFollowValue<br>TaxEfficientProduct<br>InvestorTaxReferenceType<br>TaxEfficientProduct<br>CurrentYearSubscription<br>TaxPartyRole<br>Role<br>TaxPartyRole<br>Tax<br>TaxPartyRole<br>VATRegistrationNumber<br>TaxPayer<br>TaxPartyRole | TaxEfficientProduct | LowestInvestedAmountCurrentYear |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|---------------------------------|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                     |                                 |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                     |                                 |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                     |                                 |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                     |                                 |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                     |                                 |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                     |                                 |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                     |                                 |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                     |                                 |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                     |                                 |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                     |                                 |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                     |                                 |  |

| TaxPeriod    |                 |              |
|--------------|-----------------|--------------|
| TaxPeriod    | TaxRecord       |              |
| TaxPeriod    | Year            |              |
| TaxPeriod    | Type            |              |
| TaxPeriod    | FromToDate      |              |
| TaxPeriod    | EndOfFiscalYear |              |
| TaxRecipient |                 | TaxPartyRole |
| TaxRecord    |                 |              |
| TaxRecord    | Tax             |              |
| TaxRecord    | TaxRecordType   |              |
| TaxRecord    | Category        |              |
| TaxRecord    | Status          |              |

| TaxRecord  | FormsCode             |  |
|------------|-----------------------|--|
| TaxRecord  | Period                |  |
| TaxRecord  | Amount                |  |
| TaxRecord  | CategoryDescription   |  |
| TaxVoucher |                       |  |
| TaxVoucher | RequestedTaxationRate |  |
| TaxVoucher | CreditRate            |  |
| TaxVoucher | RelatedSecurityTax    |  |
| TaxVoucher | SundryOrOtherAmount   |  |

| TaxVoucher | CreditAmount                           |  |
|------------|----------------------------------------|--|
| TaxVoucher | CashAmountBroughtForward               |  |
| TaxVoucher | CashAmountCarriedForward               |  |
| TaxVoucher | NotionalTaxAmount                      |  |
| TaxVoucher | Distribution                           |  |
| TaxVoucher | Identification                         |  |
| TaxVoucher | BargainDate                            |  |
| TaxVoucher | BargainSettlementDate                  |  |
| TaxVoucher | TaxVoucherRate                         |  |
| TaxVoucher | RecordDateHolding                      |  |
| TaxVoucher | ScripDividendReinvestmentPricePerShare |  |
| TaxVoucher | AllotedSharesCost                      |  |
|            |                                        |  |

| TaxVoucher               | ForeignExchangeTransaction |        |
|--------------------------|----------------------------|--------|
| TerminalManagementAction |                            |        |
| TerminalManagementAction | Type                       |        |
| TerminalManagementAction | Trigger                    |        |
| TerminalManagementAction | AdditionalProcess          |        |
| TerminalManagementAction | ActionResult               |        |
| TerminalManagementAction | ActionToProcess            |        |
| TerminalManagementAction | TerminalManagementSystem   |        |
| TerminalManagementSystem |                            | System |
| TerminalManagementSystem | AcceptorConfiguration      |        |
| TerminalManagementSystem | NetworkAccess              |        |
|                          |                            |        |

| TerminalManagementSystem | CardPaymentAcquiring         |                                    |
|--------------------------|------------------------------|------------------------------------|
| TerminalManagementSystem | ContactLevel                 |                                    |
| TerminalManagementSystem | ContactDateTime              |                                    |
| TerminalManagementSystem | TerminalManagerRole          |                                    |
| TerminalManagementSystem | ControlledPointOfInteraction |                                    |
| TerminalManagementSystem | Action                       |                                    |
| TerminalManagerRole      |                              | SystemPartyRole                    |
| TerminalManagerRole      | TerminalManagementSystem     |                                    |
| ThirdPartyRole           |                              | SystemPartyRole                    |
| ThirdReimbursementAgent  |                              | CashSettlementInstructionPartyRole |
|                          |                              |                                    |

| TimeFrame |                                             |  |
|-----------|---------------------------------------------|--|
| TimeFrame | TradeMinus                                  |  |
| TimeFrame | RenunciationMinus                           |  |
| TimeFrame | SubscriptionSettlementRelatedFundProcessing |  |
| TimeFrame | TradePlus                                   |  |
| TimeFrame | RenunciationPlus                            |  |
| TimeFrame | Prepayment                                  |  |

| TimeFrame  | OtherTimeFrameDescription        |  |
|------------|----------------------------------|--|
|            |                                  |  |
| TimeFrame  | RelatedProcessingCharacteristics |  |
| TimePeriod |                                  |  |
| TimePeriod | SystemAvailability               |  |
| TimePeriod | FromTime                         |  |
| TimePeriod | ToTime                           |  |
| Tolerance  |                                  |  |
| Tolerance  | RelatedUndertakingAmount         |  |
| Tolerance  | Quantity                         |  |
| Tolerance  | PlusPercent                      |  |
| Tolerance  | MinusPercent                     |  |

| Tolerance | Price                       |  |
|-----------|-----------------------------|--|
| Trade     |                             |  |
| Trade     | TradeDateTime               |  |
| Trade     | TradeCommission             |  |
| Trade     | ValueDate                   |  |
| Trade     | EndDate                     |  |
| Trade     | TradeRelatedIdentifications |  |
| Trade     | AllocationIndicator         |  |
| Trade     | CollateralisationType       |  |
| Trade     | BlockIndicator              |  |
| Trade     | SettlementNetting           |  |
| Trade     | TradePartyRole              |  |

| Trade | Obligation           |  |
|-------|----------------------|--|
| Trade | RelatedNegotiation   |  |
| Trade | GoverningDocument    |  |
| Trade | StartDate            |  |
| Trade | System               |  |
| Trade | Asset                |  |
| Trade | Market               |  |
| Trade | Guarantee            |  |
| Trade | Settlement           |  |
| Trade | Order                |  |
| Trade | Leg                  |  |
| Trade | FinancialTransaction |  |

| Trade                     | Reconciliation            |          |
|---------------------------|---------------------------|----------|
| TradeCertificate          |                           | Document |
| TradeCertificate          | CertificateType           |          |
| TradeCertificate          | InspectionDate            |          |
| TradeCertificate          | TradeCertificatePartyRole |          |
| TradeCertificate          | ProductDelivery           |          |
| TradeCertificatePartyRole |                           | Role     |
| TradeCertificatePartyRole | TradeCertificate          |          |
| TradeIdentification       |                           |          |
| TradeIdentification       | CounterpartyReference     |          |

| TradeIdentification<br>Identification                |
|------------------------------------------------------|
| TradeIdentification<br>CommonIdentification          |
| TradeIdentification<br>MatchingReference             |
| TradeIdentification<br>Trade                         |
| TradeIdentification<br>UniqueTradeIdentifier         |
| TradeIdentification<br>ClearingBrokerIdentification  |
| TradeIdentification<br>RelatedPostTradeRiskReduction |
| TradeIdentification<br>RelatedEventIdentifier        |

| TradeOriginatorRole |                      | TradePartyRole       |
|---------------------|----------------------|----------------------|
| TradeOriginatorRole | OriginatorRole       |                      |
| TradePartyRole      |                      | Role                 |
| TradePartyRole      | Account              |                      |
| TradePartyRole      | TradingPartyCapacity |                      |
| TradePartyRole      | BuyerOrSeller        |                      |
| TradePartyRole      | Trade                |                      |
| TradeRegulator      |                      | TradePartyRole       |
| TradingBranch       |                      | TreasuryTradingParty |
| TradingMarket       |                      | Market               |

| TradingMarket | TradedSecurity               |  |
|---------------|------------------------------|--|
| TradingMarket | Type                         |  |
| TradingMarket | ListedSecurity               |  |
| TradingMarket | SourceOfPrice                |  |
| TradingMarket | TradeLotSize                 |  |
| TradingMarket | MinimumTradedNominalQuantity |  |
| TradingMarket | ListingDate                  |  |
| TradingMarket | RelatedOrder                 |  |
| TradingMarket | TradingCurrency              |  |
| TradingMarket | MaximumTradedNominalQuantity |  |
| TradingMarket | StockExchange                |  |

| TradingMarket | QuoteLot                            |  |
|---------------|-------------------------------------|--|
| TradingMarket | RoundLot                            |  |
| TradingMarket | TradingSession                      |  |
| TradingMarket | ListedSecurityTradingIdentification |  |
| TradingMarket | DefaultCurrency                     |  |
| TradingMarket | FirstTradingDate                    |  |
| TradingMarket | LastTradingDate                     |  |
| TradingMarket | Issuance                            |  |
| TradingMarket | RelatedPlaceOfSettlement            |  |
|               |                                     |  |

| TradingSession |                         |  |
|----------------|-------------------------|--|
| TradingSession | TradingSessionName      |  |
| TradingSession | TimeBracket             |  |
| TradingSession | Market                  |  |
| TradingSession | Quote                   |  |
| TradingSession | SecuritiesOrder         |  |
| TradingSession | TradingSessionIndicator |  |
| TradingSession | TradingSessionPhase     |  |

| TradingSession           | USFuturesTradingSession |                 |
|--------------------------|-------------------------|-----------------|
| TradingSession           | ListTrading             |                 |
| Tranche                  |                         |                 |
| Tranche                  | Asset                   |                 |
| Tranche                  | DetachmentPoint         |                 |
| Tranche                  | AttachmentPoint         |                 |
| TransactionAdministrator |                         | SystemPartyRole |
| TransactionAdministrator | CashClearingSystem      |                 |
| TransactionAdministrator | Currency                |                 |

| TransactionAdministrator | CurrencyExchange      |  |
|--------------------------|-----------------------|--|
| TransactionAdministrator | CashManagementService |  |
| TransactionAdministrator | SettlementInstruction |  |
| TransactionRisk          |                       |  |
| TransactionRisk          | Obligation            |  |
| TransactionRisk          | ExposedAmount         |  |

| TransactionRisk   | ExposureCalculation |                         |
|-------------------|---------------------|-------------------------|
| TransferAgentRole |                     | InvestmentFundPartyRole |
| Transport         |                     |                         |
| Transport         | Incoterms           |                         |
| Transport         | Identification      |                         |
| Transport         | Packaging           |                         |

| Transport | ArrivalDateTime                |  |
|-----------|--------------------------------|--|
| Transport | PartialShipment                |  |
| Transport | TransShipment                  |  |
| Transport | ProductDelivery                |  |
| Transport | PlaceOfDeparture               |  |
| Transport | PlaceOfDestination             |  |
| Transport | TransportCharges               |  |
| Transport | FreightChargesPrepaidOrCollect |  |
| Transport | ShipmentDates                  |  |
| Transport | TransportedGoods               |  |
| Transport | PartyRole                      |  |
| Transport | TransitLocation                |  |
|           |                                |  |

| Transport       | TransportDocuments     |           |
|-----------------|------------------------|-----------|
| TransportByAir  |                        | Transport |
| TransportByAir  | AirportName            |           |
| TransportByAir  | FlightNumber           |           |
| TransportByRail |                        | Transport |
| TransportByRail | CarriageIdentification |           |
| TransportByRoad |                        | Transport |
| TransportBySea  |                        | Transport |
| TransportBySea  | VesselName             |           |
| TransportBySea  | VoyageNumber           |           |
| TransportBySea  | ChartererName          |           |
| TransportBySea  | MasterName             |           |
| TransportBySea  | OwnerName              |           |
|                 |                        |           |

| TransportBySea               | IMONumber     |                             |
|------------------------------|---------------|-----------------------------|
| TransportPartyRole           |               | Role                        |
| TransportPartyRole           | Transport     |                             |
| TreasuryManager              |               | AccountPartyRole            |
| TreasurySettlementPartyRole  |               | SettlementPartyRole         |
| TreasurySettlementPartyRole  | TreasuryTrade |                             |
| TreasurySettlementSystem     |               | System                      |
| TreasurySettlementSystem     | SystemRole    |                             |
| TreasurySettlementSystemRole |               | TreasurySettlementPartyRole |
|                              |               |                             |

| TreasurySettlementSystemRole  | System                        |                |
|-------------------------------|-------------------------------|----------------|
| TreasuryTrade                 |                               | Trade          |
| TreasuryTrade                 | TreasuryTradeSettlementStatus |                |
| TreasuryTrade                 | InformationPartyRole          |                |
| TreasuryTrade                 | TreasurySettlementPartyRole   |                |
| TreasuryTrade                 | PartyRole                     |                |
| TreasuryTrade                 | PaymentClearingCentre         |                |
| TreasuryTradePartyRole        |                               | TradePartyRole |
| TreasuryTradePartyRole        | TreasuryTrade                 |                |
| TreasuryTradeSettlementStatus |                               | Status         |
| TreasuryTradeSettlementStatus | TradeStatus                   |                |

| TreasuryTradeSettlementStatus | AllegedTrade        |                        |
|-------------------------------|---------------------|------------------------|
| TreasuryTradeSettlementStatus | TreasuryTrade       |                        |
| TreasuryTradeSettlementStatus | Settlement          |                        |
| TreasuryTradeSettlementStatus | RejectedAmount      |                        |
| TreasuryTradeSettlementStatus | SettlementSuspended |                        |
| TreasuryTradeSettlementStatus | PendingSettlement   |                        |
| TreasuryTradeSettlementStatus | SettlementDate      |                        |
| TreasuryTradeSettlementStatus | WithdrawalReason    |                        |
| TreasuryTradingParty          |                     | TreasuryTradePartyRole |
| TreasuryTradingParty          | InvestmentFund      |                        |
| Trigger                       |                     |                        |
| Trigger                       | AutomaticVariation  |                        |

| Trigger              | TriggerDate   |                            |
|----------------------|---------------|----------------------------|
| Trigger              | TriggerEvent  |                            |
| TripartyAgent        |               | CollateralPartyRole        |
| TrusteeRole          |               | InvestmentAccountPartyRole |
| UTCOffset            |               |                            |
| UTCOffset            | Sign          |                            |
| UTCOffset            | NumberOfHours |                            |
| UTCOffset            | Location      |                            |
| UltimateCreditorRole |               | PaymentObligationPartyRole |
| UltimateDebtorRole   |               | PaymentObligationPartyRole |
|                      |               |                            |

| UmbrellaFund          |                               |  |
|-----------------------|-------------------------------|--|
| UmbrellaFund          | Name                          |  |
| UmbrellaFund          | SubFund                       |  |
| UnderlyingRatio       |                               |  |
| UnderlyingRatio       | SecuritiesConversion          |  |
| UnderlyingRatio       | UnderlyingQuantityDenominator |  |
| UnderlyingRatio       | UnderlyingQuantityNumerator   |  |
| UnderlyingTransaction |                               |  |
| UnderlyingTransaction | Undertaking                   |  |

| UnderlyingTransaction | Type                     |  |
|-----------------------|--------------------------|--|
| UnderlyingTransaction | Identification           |  |
| UnderlyingTransaction | IssueDate                |  |
| UnderlyingTransaction | TenderClosingDate        |  |
| UnderlyingTransaction | TotalAmount              |  |
| UnderlyingTransaction | ContractAmountPercentage |  |
| UnderlyingTransaction | CommercialTrade          |  |
| Undertaking           |                          |  |
| Undertaking           | ElectronicSignature      |  |
| Undertaking           | UndertakingStatus        |  |
| Undertaking           | Identification           |  |

| Undertaking | Demand               |  |
|-------------|----------------------|--|
| Undertaking | TerminationDate      |  |
| Undertaking | UndertakingAmount    |  |
| Undertaking | Expiry               |  |
| Undertaking | PartyRole            |  |
| Undertaking | UndertakingAmendment |  |
| Undertaking | SpecifiedDocument    |  |
| Undertaking | DateOfAdvice         |  |
| Undertaking | Purpose              |  |
| Undertaking | UndertakingName      |  |
| Undertaking | Type                 |  |

| Undertaking | ConfirmationIndicator          |  |
|-------------|--------------------------------|--|
| Undertaking | CounterUndertakingIndicator    |  |
| Undertaking | RelatedChargesPayableBy        |  |
| Undertaking | StandardClaimDocumentIndicator |  |
| Undertaking | UnderlyingTransaction          |  |
| Undertaking | ModelForm                      |  |
| Undertaking | MultipleDemandIndicator        |  |
| Undertaking | PartialDemandIndicator         |  |
| Undertaking | TransferIndicator              |  |

| Undertaking              | PredefinedVariation  |                      |
|--------------------------|----------------------|----------------------|
| Undertaking              | Charges              |                      |
| Undertaking              | Presentation         |                      |
| Undertaking              | UndertakingExtension |                      |
| UndertakingAdvisingParty |                      | UndertakingPartyRole |
| UndertakingAmount        |                      |                      |
| UndertakingAmount        | Undertaking          |                      |
| UndertakingAmount        | Amount               |                      |
| UndertakingAmount        | Tolerance            |                      |
| UndertakingAmount        | BalanceAmount        |                      |

| UndertakingAmount<br>Type                |                      |
|------------------------------------------|----------------------|
| UndertakingAmount<br>Interest            |                      |
| UndertakingApplicant                     | UndertakingPartyRole |
| UndertakingBeneficiary                   | UndertakingPartyRole |
| UndertakingConfirmer                     | UndertakingPartyRole |
| UndertakingDeliveryToParty               | UndertakingPartyRole |
| UndertakingDocument<br>FinancialDocument |                      |
| UndertakingDocument<br>DocumentType      |                      |
| UndertakingDocument<br>Format            |                      |
| UndertakingDocument<br>Undertaking       |                      |
| UndertakingDocument<br>CopyIndicator     |                      |
| UndertakingDocument<br>Demand            |                      |
| UndertakingExtension                     |                      |

| UndertakingExtension        | Undertaking                     |                      |
|-----------------------------|---------------------------------|----------------------|
| UndertakingExtension        | AutoExtensionPeriod             |                      |
| UndertakingExtension        | AutoExtensionFinalExpiryDate    |                      |
| UndertakingExtension        | NonExtensionNoticePeriod        |                      |
| UndertakingExtension        | NonExtensionIndicator           |                      |
| UndertakingExtension        | AutoExtensionNotificationPeriod |                      |
| UndertakingExtension        | NotificationRecipientType       |                      |
| UndertakingInstructingParty |                                 | UndertakingPartyRole |
| UndertakingIssuer           |                                 | UndertakingPartyRole |
| UndertakingPartyRole        |                                 | Role                 |

| UndertakingPartyRole           | Undertaking                   |                      |
|--------------------------------|-------------------------------|----------------------|
| UndertakingPlaceOfPresentation |                               | UndertakingPartyRole |
| UndertakingPlaceOfPresentation | PresentationUnderConfirmation |                      |
| UndertakingPresenter           |                               | UndertakingPartyRole |
| UndertakingStatus              |                               | Status               |
| UndertakingStatus              | Undertaking                   |                      |
| UndertakingStatus              | DemandStatus                  |                      |
| UndertakingStatus              | Status                        |                      |
| UndertakingStatus              | UndertakingStatusReason       |                      |
| UndertakingStatus              | StatusCategory                |                      |
| UndertakingStatus              | PresentationStatus            |                      |
| UndertakingStatusReason        |                               | StatusReason         |
| UndertakingStatusReason        | Discrepancy                   |                      |
|                                |                               |                      |

| UndertakingStatusReason    | UndertakingStatus         |                      |
|----------------------------|---------------------------|----------------------|
| UndertakingStatusReason    | TerminationReason         |                      |
| UndertakingStatusReason    | DemandRefusalStatusReason |                      |
| UndertakingStatusReason    | SettlementReason          |                      |
| UndertakingUltimateObligor |                           | UndertakingPartyRole |
| UndertakingUltimateObligor | CashAccount               |                      |
| UnderwriterRole            |                           | SecuritiesPartyRole  |
| ValidatingPartyRole        |                           | DocumentPartyRole    |
| ValuationStatistics        |                           |                      |
| ValuationStatistics        | Currency                  |                      |
|                            |                           |                      |

| ValuationStatistics | PriceTypeChangeBasis        |  |
|---------------------|-----------------------------|--|
| ValuationStatistics | PriceChange                 |  |
| ValuationStatistics | Yield                       |  |
| ValuationStatistics | HighestPriceValue           |  |
| ValuationStatistics | LowestPriceValue            |  |
| ValuationStatistics | Period                      |  |
| ValuationStatistics | NetAssetValueCalculation    |  |
| ValuationStatistics | NetAssetValueChangeRate     |  |
| VariableInterest    |                             |  |
| VariableInterest    | VariableRateChangeFrequency |  |
|                     |                             |  |

| VariableInterest<br>FixingDate<br>VariableInterest<br>InterestCalculation<br>VariableInterest<br>ReportingDate<br>VariableInterest<br>ResetDate<br>VariableInterest<br>Arrears<br>VariableInterest<br>Index<br>VariableInterest<br>YieldCalculation<br>VariableInterest<br>BenchmarkReference |  |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                               |  |  |

| VariableInterest         | EstimatedInterestRate |                      |
|--------------------------|-----------------------|----------------------|
| VariableInterest         | VariableRateValueDate |                      |
| VariableInterest         | LifeCalculation       |                      |
| VariableInterest         | DurationCalculation   |                      |
| VariationMarginTerm      |                       | ExposureTerm         |
| VariationMarginTerm      | ThresholdAmount       |                      |
| VariationMarginTerm      | ThresholdType         |                      |
| VoluntaryCorporateAction |                       | CorporateActionEvent |
| Vote                     |                       |                      |
| Vote                     | VoteRequest           |                      |
| Vote                     | For                   |                      |
|                          |                       |                      |

| Vote | Against           |  |
|------|-------------------|--|
| Vote | Abstain           |  |
| Vote | Withhold          |  |
| Vote | WithManagement    |  |
| Vote | AgainstManagement |  |
| Vote | Resolution        |  |
| Vote | NoAction          |  |
| Vote | Result            |  |
| Vote | TwoYears          |  |
| Vote | OneYear           |  |
| Vote | Withdrawn         |  |
| Vote | ThreeYears        |  |

| Vote<br>Blank<br>Vote<br>VoteReceiptDateTime<br>VoteDeadline<br>MeetingDeadline<br>VoteInstructionRequest<br>VoteInstructionRequest<br>MeetingInstruction<br>VoteInstructionRequest<br>VotePerResolution<br>VoteInstructionRequest<br>Discretionary<br>VoteInstructionRequest<br>GlobalVoteInstruction<br>VoteInstructionRequest<br>VoteForMeetingResolution<br>VoteInstructionRequest<br>VoteExecutionConfirmation<br>VoteInstructionRequest<br>RelatedProxyAppointment |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |

| VoteRegistrationDeadline |                    | MeetingDeadline |
|--------------------------|--------------------|-----------------|
| VoteResult               |                    |                 |
| VoteResult               | Vote               |                 |
| VoteResult               | Accepted           |                 |
| VoteResult               | VoteDissemination  |                 |
| VoteResult               | TotalVotesCast     |                 |
| VoteResult               | ModalityOfCounting |                 |
| VoteRevocabilityDeadline |                    | MeetingDeadline |
| VoteWithPremiumDeadline  |                    | MeetingDeadline |
|                          |                    |                 |

| VotingCondition<br>VotingCondition<br>SecuritiesQuantityRequiredToVote<br>VotingCondition<br>PartialVoteAllowed<br>VotingCondition<br>SplitVoteAllowed<br>VotingCondition<br>VoteLocation<br>VotingCondition<br>BeneficialOwnerDisclosure<br>VotingCondition<br>IncentivePremium<br>VotingCondition<br>VoteInstructionType<br>VotingCondition<br>StandingVotingInstruction |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                            |  |  |
|                                                                                                                                                                                                                                                                                                                                                                            |  |  |

| VotingCondition | VotingPremiumAmount           |                  |
|-----------------|-------------------------------|------------------|
| VotingCondition | VotingPremiumRate             |                  |
| VotingCondition | Meeting                       |                  |
| VotingCondition | PreviousInstructionInvalidity |                  |
| VotingPartyRole |                               | MeetingPartyRole |
| Warrant         |                               | Security         |
| Warrant         | SubscriptionPrice             |                  |
| Warrant         | Multiplier                    |                  |
| Warrant         | Style                         |                  |
| Warrant         | WarrantParity                 |                  |
|                 |                               |                  |

|                      | AssetPartyRole |
|----------------------|----------------|
|                      |                |
| RedemptionPrice      |                |
| Value                |                |
| CalculationType      |                |
| ValueDate            |                |
| ValuePeriod          |                |
| YieldCalculationDate |                |
| YieldRange           |                |
| VariableInterest     |                |
|                      |                |

## **Traces**

| Message Component Name        | Message Element Name         | Type Trace To         | Is<br>Technical | Trace To Business Component |
|-------------------------------|------------------------------|-----------------------|-----------------|-----------------------------|
| AccountIdentification4Choice  | IBAN                         |                       | False           | AccountIdentification       |
| AccountIdentification4Choice  | Other                        | AccountIdentification | False           | AccountIdentification       |
| AccountSchemeName1Choice      |                              |                       | False           | Scheme                      |
| AccountSchemeName1Choice      | Code                         |                       | False           | Scheme                      |
| AccountSchemeName1Choice      | Proprietary                  |                       | False           | Scheme                      |
| AdditionalDateTime1           |                              |                       | False           |                             |
| AdditionalDateTime1           | AcceptanceDateTime           |                       | False           | PaymentExecution            |
| AdditionalDateTime1           | ExpiryDateTime               |                       | False           |                             |
| AdditionalDateTime1           | PoolingAdjustmentDate        |                       | False           |                             |
| AddressType3Choice            |                              |                       | True            |                             |
| AddressType3Choice            | Code                         |                       | True            |                             |
| AddressType3Choice            | Proprietary                  | GenericIdentification | True            |                             |
| AmendmentInformationDetails15 |                              |                       | False           |                             |
| AmendmentInformationDetails15 | OriginalCreditorAgent        | Organisation          | False           |                             |
| AmendmentInformationDetails15 | OriginalCreditorAgentAccount | CashAccount           | False           |                             |
|                               |                              |                       |                 |                             |

| AmendmentInformationDetails15                | OriginalCreditorSchemeIdentification | PartyIdentificationInformation | False | Party              |           | Identification             |  |
|----------------------------------------------|--------------------------------------|--------------------------------|-------|--------------------|-----------|----------------------------|--|
| AmendmentInformationDetails15                | OriginalDebtor                       | PartyIdentificationInformation | False | Party              |           | Identification             |  |
| AmendmentInformationDetails15                | OriginalDebtorAccount                | CashAccount                    | False | PaymentPartyRole   |           | CashAccount                |  |
| AmendmentInformationDetails15                | OriginalDebtorAgent                  | Organisation                   | False | Organisation       |           | OrganisationIdentification |  |
| AmendmentInformationDetails15                | OriginalDebtorAgentAccount           | CashAccount                    | False | PaymentPartyRole   |           | CashAccount                |  |
| AmendmentInformationDetails15                | OriginalFinalCollectionDate          |                                | False | DirectDebitMandate |           | FinalCollectionDate        |  |
| AmendmentInformationDetails15                | OriginalFrequency                    |                                | False | Mandate            | Frequency |                            |  |
| AmendmentInformationDetails15                | OriginalMandateIdentification        |                                | False | Mandate            |           | MandateIdentification      |  |
| AmendmentInformationDetails15                | OriginalReason                       |                                | False | Agreement          |           | Description                |  |
| AmendmentInformationDetails15                | OriginalTrackingDays                 |                                | False | Mandate            |           | TrackingDays               |  |
| AmountType4Choice                            |                                      |                                | False | Payment            |           |                            |  |
| AmountType4Choice                            | EquivalentAmount                     | Payment                        | False | Payment            |           | EquivalentAmount           |  |
| AmountType4Choice                            | InstructedAmount                     |                                | False | Payment            |           | InstructedAmount           |  |
| Authorisation1Choice                         |                                      |                                | True  |                    |           |                            |  |
| Authorisation1Choice                         | Code                                 |                                | True  |                    |           |                            |  |
| Authorisation1Choice                         | Proprietary                          |                                | True  |                    |           |                            |  |
| BranchAndFinancialInstitutionIdentification8 |                                      |                                | False | Organisation       |           |                            |  |
| BranchAndFinancialInstitutionIdentification8 | BranchIdentification                 | OrganisationIdentification     | False | Organisation       |           | OrganisationIdentification |  |

| BranchAndFinancialInstitutionIdentification8 | FinancialInstitutionIdentification | OrganisationIdentification | False<br>Organisation               |
|----------------------------------------------|------------------------------------|----------------------------|-------------------------------------|
| BranchData5                                  |                                    |                            | False<br>OrganisationIdentification |
| BranchData5                                  | Identification                     |                            | False<br>GenericIdentification      |
| BranchData5                                  | LEI                                |                            | True                                |
| BranchData5                                  | Name                               |                            | False<br>PartyName                  |
| BranchData5                                  | PostalAddress                      | PostalAddress              | False                               |
| CashAccount40                                |                                    |                            | False<br>CashAccount                |
| CashAccount40                                | Currency                           |                            | False<br>Account                    |
| CashAccount40                                | Identification                     | AccountIdentification      | False<br>Account                    |
| CashAccount40                                | Name                               |                            | False<br>AccountIdentification      |
| CashAccount40                                | Proxy                              | AccountIdentification      | False<br>Account                    |
| CashAccount40                                | Type                               | CashAccount                | False<br>CashAccount                |
| CashAccountType2Choice                       |                                    |                            | False<br>CashAccount                |
| CashAccountType2Choice                       | Code                               |                            | False<br>CashAccount                |
| CashAccountType2Choice                       | Proprietary                        |                            | False<br>CashAccount                |
| CategoryPurpose1Choice                       |                                    |                            | False<br>Payment                    |
| CategoryPurpose1Choice                       | Code                               |                            | False<br>PaymentProcessing          |
| CategoryPurpose1Choice                       | Proprietary                        |                            | False<br>PaymentProcessing          |
| Charges16                                    |                                    |                            | False<br>Charges                    |

| Charges16                           | Agent                        | Organisation          | False |
|-------------------------------------|------------------------------|-----------------------|-------|
| Charges16                           | Amount                       |                       | False |
| Charges16                           | Type                         | Charges               | False |
| ChargeType3Choice                   |                              |                       | False |
| ChargeType3Choice                   | Code                         |                       | False |
| ChargeType3Choice                   | Proprietary                  | GenericIdentification | False |
| ClearingSystemIdentification2Choice |                              |                       | False |
| ClearingSystemIdentification2Choice | Code                         |                       | False |
| ClearingSystemIdentification2Choice | Proprietary                  |                       | False |
| ClearingSystemIdentification3Choice |                              |                       | False |
| ClearingSystemIdentification3Choice | Code                         |                       | False |
| ClearingSystemIdentification3Choice | Proprietary                  |                       | False |
| ClearingSystemMemberIdentification2 |                              |                       | False |
| ClearingSystemMemberIdentification2 | ClearingSystemIdentification | CashClearingSystem    | False |
| ClearingSystemMemberIdentification2 | MemberIdentification         |                       | False |
| Contact13                           |                              |                       | False |
| Contact13                           | Department                   |                       | False |
| Contact13                           | EmailAddress                 |                       | False |

| Contact13                     | EmailPurpose      |              | True                                    |
|-------------------------------|-------------------|--------------|-----------------------------------------|
| Contact13                     | FaxNumber         |              | False<br>PhoneAddress                   |
| Contact13                     | JobTitle          |              | False<br>Person                         |
| Contact13                     | MobileNumber      |              | False<br>PhoneAddress                   |
| Contact13                     | Name              |              | False<br>PartyName                      |
| Contact13                     | NamePrefix        |              | False                                   |
| Contact13                     | Other             | ContactPoint | False<br>PartyIdentificationInformation |
| Contact13                     | PhoneNumber       |              | False<br>PhoneAddress                   |
| Contact13                     | PreferredMethod   |              | False<br>Party                          |
| Contact13                     | Responsibility    |              | False<br>Person                         |
| Contact13                     | URLAddress        |              | False                                   |
| CreditorReferenceInformation3 |                   |              | False                                   |
| CreditorReferenceInformation3 | Reference         |              | False<br>PaymentIdentification          |
| CreditorReferenceInformation3 | Type              | Document     | True                                    |
| CreditorReferenceType2Choice  |                   |              | False<br>Document                       |
| CreditorReferenceType2Choice  | Code              |              | False<br>Document                       |
| CreditorReferenceType2Choice  | Proprietary       |              | False<br>Document                       |
| CreditorReferenceType3        |                   |              | False<br>Document                       |
| CreditorReferenceType3        | CodeOrProprietary | Document     | False                                   |
| CreditorReferenceType3        | Issuer            |              | False                                   |

|                                   |              | False | CreditTransferMandate |
|-----------------------------------|--------------|-------|-----------------------|
| DateOfSignature                   |              | False | Agreement             |
| DateOfVerification                |              | False | CreditTransferMandate |
| ElectronicSignature               |              | False | CreditTransferMandate |
| FinalPaymentDate                  |              | False | CreditTransferMandate |
| FirstPaymentDate                  |              | False | CreditTransferMandate |
| Frequency                         |              | False | Mandate               |
| MandateIdentification             |              | False | Mandate               |
| Reason                            |              | False | CreditTransferMandate |
| Type                              | Mandate      | False | Mandate               |
|                                   |              | False | Payment               |
| BatchBooking                      |              | True  |                       |
| CreditIdentification              |              | True  |                       |
| Creditor                          | Organisation | False | Organisation          |
| CreditorAccount                   | CashAccount  | False | PaymentPartyRole      |
| CreditorAgent                     | Organisation | False | Organisation          |
| CreditorAgentAccount              | CashAccount  | False | PaymentPartyRole      |
| DirectDebitTransactionInformation | DirectDebit  | False |                       |
| InstructedAgent                   |              |       | Organisation          |
|                                   |              |       | Organisation<br>False |

| CreditTransferTransaction66 | InstructingAgent               | Organisation      | False | Organisation       |
|-----------------------------|--------------------------------|-------------------|-------|--------------------|
| CreditTransferTransaction66 | InstructionForCreditorAgent    | Payment           | False | Payment            |
| CreditTransferTransaction66 | InterbankSettlementDate        |                   | False | CashSettlement     |
| CreditTransferTransaction66 | IntermediaryAgent1             | Organisation      | False | Organisation       |
| CreditTransferTransaction66 | IntermediaryAgent1Account      | CashAccount       | False | PaymentPartyRole   |
| CreditTransferTransaction66 | IntermediaryAgent2             | Organisation      | False | Organisation       |
| CreditTransferTransaction66 | IntermediaryAgent2Account      | CashAccount       | False | PaymentPartyRole   |
| CreditTransferTransaction66 | IntermediaryAgent3             | Organisation      | False | Organisation       |
| CreditTransferTransaction66 | IntermediaryAgent3Account      | CashAccount       | False | PaymentPartyRole   |
| CreditTransferTransaction66 | PaymentTypeInformation         | PaymentProcessing | False | PaymentExecution   |
| CreditTransferTransaction66 | SettlementTimeIndication       | CashSettlement    | False | PaymentInstruction |
| CreditTransferTransaction66 | SupplementaryData              |                   | True  |                    |
| CreditTransferTransaction66 | TotalInterbankSettlementAmount |                   | False | CashSettlement     |
| CreditTransferTransaction66 | UltimateCreditor               | Organisation      | False | Organisation       |
| CreditTransferTransaction67 |                                |                   | False | CreditTransfer     |

| CreditTransferTransaction67 | Creditor                    | Organisation       | False | Party              |
|-----------------------------|-----------------------------|--------------------|-------|--------------------|
| CreditTransferTransaction67 | CreditorAccount             | CashAccount        | False | PaymentPartyRole   |
| CreditTransferTransaction67 | CreditorAgent               | Organisation       | False | Organisation       |
| CreditTransferTransaction67 | CreditorAgentAccount        | CashAccount        | False | PaymentPartyRole   |
| CreditTransferTransaction67 | Debtor                      | Organisation       | False | Party              |
| CreditTransferTransaction67 | DebtorAccount               | CashAccount        | False | PaymentPartyRole   |
| CreditTransferTransaction67 | DebtorAgent                 | Organisation       | False | Party              |
| CreditTransferTransaction67 | DebtorAgentAccount          | CashAccount        | False | PaymentPartyRole   |
| CreditTransferTransaction67 | ExpiryDateTime              |                    | False |                    |
| CreditTransferTransaction67 | InstructedAgent             | Organisation       | False | Organisation       |
| CreditTransferTransaction67 | InstructingAgent            | Organisation       | False | Organisation       |
| CreditTransferTransaction67 | InstructionForCreditorAgent | Payment            | False | Payment            |
| CreditTransferTransaction67 | InstructionForNextAgent     | PaymentInstruction | False | PaymentInstruction |
| CreditTransferTransaction67 | InterbankSettlementAmount   |                    | False | CashSettlement     |
| CreditTransferTransaction67 | InterbankSettlementDate     |                    | False |                    |
| CreditTransferTransaction67 | IntermediaryAgent1          | Organisation       | False |                    |
|                             |                             |                    |       |                    |

| CreditTransferTransaction67 | IntermediaryAgent1Account        | CashAccount           | False | PaymentPartyRole |
|-----------------------------|----------------------------------|-----------------------|-------|------------------|
| CreditTransferTransaction67 | IntermediaryAgent2               | Organisation          | False | Organisation     |
| CreditTransferTransaction67 | IntermediaryAgent2Account        | CashAccount           | False | PaymentPartyRole |
| CreditTransferTransaction67 | IntermediaryAgent3               | Organisation          | False | Organisation     |
| CreditTransferTransaction67 | IntermediaryAgent3Account        | CashAccount           | False | PaymentPartyRole |
| CreditTransferTransaction67 | PaymentIdentification            | PaymentIdentification | False | Payment          |
| CreditTransferTransaction67 | PaymentSignature                 |                       | True  |                  |
| CreditTransferTransaction67 | PaymentTypeInformation           | PaymentProcessing     | False |                  |
| CreditTransferTransaction67 | PreviousInstructingAgent1        | Organisation          | False | Organisation     |
| CreditTransferTransaction67 | PreviousInstructingAgent1Account | CashAccount           | False |                  |
| CreditTransferTransaction67 | PreviousInstructingAgent2        | Organisation          | False |                  |
| CreditTransferTransaction67 | PreviousInstructingAgent2Account | CashAccount           | False | PaymentPartyRole |
| CreditTransferTransaction67 | PreviousInstructingAgent3        | Organisation          | False |                  |
| CreditTransferTransaction67 | PreviousInstructingAgent3Account | CashAccount           | False |                  |
| CreditTransferTransaction67 | Purpose                          | PaymentObligation     | False |                  |
| CreditTransferTransaction67 | RemittanceInformation            | Document              | False |                  |
| CreditTransferTransaction67 | SettlementPriority               |                       | False |                  |

| CreditTransferTransaction67 | SettlementTimeIndication                     | CashSettlement                 | False | PaymentInstruction |
|-----------------------------|----------------------------------------------|--------------------------------|-------|--------------------|
| CreditTransferTransaction67 | SettlementTimeRequest                        | SettlementTimeRequest          | False | Payment            |
| CreditTransferTransaction67 | SupplementaryData                            |                                | True  |                    |
| CreditTransferTransaction67 | UltimateCreditor                             | Organisation                   | False | Party              |
| CreditTransferTransaction67 | UltimateDebtor                               | Organisation                   | False | Party              |
| CreditTransferTransaction67 | UnderlyingAllocation                         | IndividualPayment              | False |                    |
| CreditTransferTransaction67 | UnderlyingCustomerCreditTransfer             | CreditTransfer                 | False |                    |
| CreditTransferTransaction67 | UnderlyingFinancialInstitutionCreditTransfer | CreditTransfer                 | False |                    |
| CreditTransferTransaction68 |                                              |                                | False | CreditTransfer     |
| CreditTransferTransaction68 | Creditor                                     | PartyIdentificationInformation | False | Party              |
| CreditTransferTransaction68 | CreditorAccount                              | CashAccount                    | False | PaymentPartyRole   |
| CreditTransferTransaction68 | CreditorAgent                                | Organisation                   | False | Organisation       |
| CreditTransferTransaction68 | CreditorAgentAccount                         | CashAccount                    | False | PaymentPartyRole   |
| CreditTransferTransaction68 | Debtor                                       | PartyIdentificationInformation | False | Party              |
| CreditTransferTransaction68 | DebtorAccount                                | CashAccount                    | False | PaymentPartyRole   |
| CreditTransferTransaction68 | DebtorAgent                                  | Organisation                   | False | Party              |
| CreditTransferTransaction68 | DebtorAgentAccount                           | CashAccount                    | False | PaymentPartyRole   |

| CreditTransferTransaction68 | InitiatingParty                  | PartyIdentificationInformation | False | Party              |
|-----------------------------|----------------------------------|--------------------------------|-------|--------------------|
| CreditTransferTransaction68 | InstructedAmount                 |                                | False | Payment            |
| CreditTransferTransaction68 | InstructionForCreditorAgent      | Payment                        | False | Payment            |
| CreditTransferTransaction68 | InstructionForNextAgent          | PaymentInstruction             | False | PaymentInstruction |
| CreditTransferTransaction68 | IntermediaryAgent1               | Organisation                   | False | Organisation       |
| CreditTransferTransaction68 | IntermediaryAgent1Account        | CashAccount                    | False | PaymentPartyRole   |
| CreditTransferTransaction68 | IntermediaryAgent2               | Organisation                   | False | Organisation       |
| CreditTransferTransaction68 | IntermediaryAgent2Account        | CashAccount                    | False | PaymentPartyRole   |
| CreditTransferTransaction68 | IntermediaryAgent3               | Organisation                   | False |                    |
| CreditTransferTransaction68 | IntermediaryAgent3Account        | CashAccount                    | False | PaymentPartyRole   |
| CreditTransferTransaction68 | PaymentIdentification            | PaymentIdentification          | False | Payment            |
| CreditTransferTransaction68 | PaymentTypeInformation           | PaymentProcessing              | False | PaymentExecution   |
| CreditTransferTransaction68 | PreviousInstructingAgent1        | Organisation                   | False | Organisation       |
| CreditTransferTransaction68 | PreviousInstructingAgent1Account | CashAccount                    | False | PaymentPartyRole   |
| CreditTransferTransaction68 | PreviousInstructingAgent2        | Organisation                   | False | Organisation       |
| CreditTransferTransaction68 | PreviousInstructingAgent2Account | CashAccount                    | False | PaymentPartyRole   |
|                             |                                  |                                |       |                    |

| CreditTransferTransaction68 | PreviousInstructingAgent3        | Organisation                   | False | Organisation      |
|-----------------------------|----------------------------------|--------------------------------|-------|-------------------|
| CreditTransferTransaction68 | PreviousInstructingAgent3Account | CashAccount                    | False | PaymentPartyRole  |
| CreditTransferTransaction68 | Purpose                          | PaymentObligation              | False | PaymentObligation |
| CreditTransferTransaction68 | RemittanceInformation            | Document                       | False | PaymentObligation |
| CreditTransferTransaction68 | Tax                              | Tax                            | False | Payment           |
| CreditTransferTransaction68 | UltimateCreditor                 | PartyIdentificationInformation | False | Party             |
| CreditTransferTransaction68 | UltimateDebtor                   | PartyIdentificationInformation | False | Party             |
| CreditTransferTransaction69 |                                  |                                | False | CreditTransfer    |
| CreditTransferTransaction69 | Creditor                         | Organisation                   | False | Party             |
| CreditTransferTransaction69 | CreditorAccount                  | CashAccount                    | False | PaymentPartyRole  |
| CreditTransferTransaction69 | CreditorAgent                    | Organisation                   | False | Organisation      |
| CreditTransferTransaction69 | CreditorAgentAccount             | CashAccount                    | False | PaymentPartyRole  |
| CreditTransferTransaction69 | Debtor                           | Organisation                   | False | Party             |
| CreditTransferTransaction69 | DebtorAccount                    | CashAccount                    | False | PaymentPartyRole  |
| CreditTransferTransaction69 | DebtorAgent                      | Organisation                   | False | Party             |
| CreditTransferTransaction69 | DebtorAgentAccount               | CashAccount                    | False | PaymentPartyRole  |
| CreditTransferTransaction69 | ExpiryDateTime                   |                                | False |                   |

| CreditTransferTransaction69 | InstructedAgent             | Organisation          | False | Organisation       |
|-----------------------------|-----------------------------|-----------------------|-------|--------------------|
| CreditTransferTransaction69 | InstructingAgent            | Organisation          | False | Organisation       |
| CreditTransferTransaction69 | InstructionForCreditorAgent | Payment               | False | Payment            |
| CreditTransferTransaction69 | InstructionForNextAgent     | PaymentInstruction    | False | PaymentInstruction |
| CreditTransferTransaction69 | InterbankSettlementAmount   |                       | False |                    |
| CreditTransferTransaction69 | InterbankSettlementDate     |                       | False |                    |
| CreditTransferTransaction69 | IntermediaryAgent1          | Organisation          | False |                    |
| CreditTransferTransaction69 | IntermediaryAgent1Account   | CashAccount           | False |                    |
| CreditTransferTransaction69 | IntermediaryAgent2          | Organisation          | False |                    |
| CreditTransferTransaction69 | IntermediaryAgent2Account   | CashAccount           | False | PaymentPartyRole   |
| CreditTransferTransaction69 | IntermediaryAgent3          | Organisation          | False | Organisation       |
| CreditTransferTransaction69 | IntermediaryAgent3Account   | CashAccount           | False | PaymentPartyRole   |
| CreditTransferTransaction69 | PaymentIdentification       | PaymentIdentification | False | Payment            |
| CreditTransferTransaction69 | PaymentSignature            |                       | True  |                    |
| CreditTransferTransaction69 | PaymentTypeInformation      | PaymentProcessing     | False | PaymentExecution   |
| CreditTransferTransaction69 | PreviousInstructingAgent1   | Organisation          | False |                    |
|                             |                             |                       |       |                    |

| CreditTransferTransaction69 | PreviousInstructingAgent1Account | CashAccount           | False<br>PaymentPartyRole   |
|-----------------------------|----------------------------------|-----------------------|-----------------------------|
| CreditTransferTransaction69 | PreviousInstructingAgent2        | Organisation          | False<br>Organisation       |
| CreditTransferTransaction69 | PreviousInstructingAgent2Account | CashAccount           | False<br>PaymentPartyRole   |
| CreditTransferTransaction69 | PreviousInstructingAgent3        | Organisation          | False<br>Organisation       |
| CreditTransferTransaction69 | PreviousInstructingAgent3Account | CashAccount           | False<br>PaymentPartyRole   |
| CreditTransferTransaction69 | Purpose                          | PaymentObligation     | False<br>PaymentProcessing  |
| CreditTransferTransaction69 | RemittanceInformation            | Document              | False<br>PaymentObligation  |
| CreditTransferTransaction69 | SettlementPriority               |                       | False<br>PaymentProcessing  |
| CreditTransferTransaction69 | SettlementTimeIndication         | CashSettlement        | False<br>PaymentInstruction |
| CreditTransferTransaction69 | SettlementTimeRequest            | SettlementTimeRequest | False<br>Payment            |
| CreditTransferTransaction69 | UltimateCreditor                 | Organisation          | False<br>Party              |
| CreditTransferTransaction69 | UltimateDebtor                   | Organisation          | False<br>Party              |
| CreditTransferTransaction69 | UnderlyingAllocation             | IndividualPayment     | False                       |
| CreditTransferTransaction70 |                                  |                       | False<br>CreditTransfer     |
| CreditTransferTransaction70 | AdditionalDateTime               | PaymentExecution      | True                        |
| CreditTransferTransaction70 | AgreedRate                       | CurrencyExchange      | True                        |
| CreditTransferTransaction70 | ChargeBearer                     |                       | False<br>Charges            |

| CreditTransferTransaction70 | ChargesInformation          | Charges                        | False |                  |
|-----------------------------|-----------------------------|--------------------------------|-------|------------------|
| CreditTransferTransaction70 | Creditor                    | PartyIdentificationInformation | False | Party            |
| CreditTransferTransaction70 | CreditorAccount             | CashAccount                    | False | PaymentPartyRole |
| CreditTransferTransaction70 | CreditorAgent               | Organisation                   | False | Organisation     |
| CreditTransferTransaction70 | CreditorAgentAccount        | CashAccount                    | False | PaymentPartyRole |
| CreditTransferTransaction70 | Debtor                      | PartyIdentificationInformation | False | Party            |
| CreditTransferTransaction70 | DebtorAccount               | CashAccount                    | False | PaymentPartyRole |
| CreditTransferTransaction70 | DebtorAgent                 | Organisation                   | False | Party            |
| CreditTransferTransaction70 | DebtorAgentAccount          | CashAccount                    | False | PaymentPartyRole |
| CreditTransferTransaction70 | ExchangeRate                |                                | False |                  |
| CreditTransferTransaction70 | InitiatingParty             | PartyIdentificationInformation | False | Party            |
| CreditTransferTransaction70 | InstructedAgent             | Organisation                   | False | Organisation     |
| CreditTransferTransaction70 | InstructedAmount            |                                | False | Payment          |
| CreditTransferTransaction70 | InstructingAgent            | Organisation                   | False | Organisation     |
| CreditTransferTransaction70 | InstructionForCreditorAgent | Payment                        | False | Payment          |
| CreditTransferTransaction70 | InstructionForNextAgent     | PaymentInstruction             | False |                  |

| CreditTransferTransaction70 | InterbankSettlementAmount        |                       | False | CashSettlement   |
|-----------------------------|----------------------------------|-----------------------|-------|------------------|
| CreditTransferTransaction70 | InterbankSettlementDate          |                       | False | CashSettlement   |
| CreditTransferTransaction70 | IntermediaryAgent1               | Organisation          | False | Organisation     |
| CreditTransferTransaction70 | IntermediaryAgent1Account        | CashAccount           | False | PaymentPartyRole |
| CreditTransferTransaction70 | IntermediaryAgent2               | Organisation          | False | Organisation     |
| CreditTransferTransaction70 | IntermediaryAgent2Account        | CashAccount           | False | PaymentPartyRole |
| CreditTransferTransaction70 | IntermediaryAgent3               | Organisation          | False | Organisation     |
| CreditTransferTransaction70 | IntermediaryAgent3Account        | CashAccount           | False | PaymentPartyRole |
| CreditTransferTransaction70 | MandateRelatedInformation        | CreditTransferMandate | False | MandatePartyRole |
| CreditTransferTransaction70 | PaymentIdentification            | PaymentIdentification | False | Payment          |
| CreditTransferTransaction70 | PaymentSignature                 |                       | True  |                  |
| CreditTransferTransaction70 | PaymentTypeInformation           | PaymentProcessing     | False | PaymentExecution |
| CreditTransferTransaction70 | PreviousInstructingAgent1        | Organisation          | False | Organisation     |
| CreditTransferTransaction70 | PreviousInstructingAgent1Account | CashAccount           | False | PaymentPartyRole |
| CreditTransferTransaction70 | PreviousInstructingAgent2        | Organisation          | False | Organisation     |
| CreditTransferTransaction70 | PreviousInstructingAgent2Account | CashAccount           | False | PaymentPartyRole |

| CreditTransferTransaction70 | PreviousInstructingAgent3        | Organisation                   | False<br>Organisation         |
|-----------------------------|----------------------------------|--------------------------------|-------------------------------|
| CreditTransferTransaction70 | PreviousInstructingAgent3Account | CashAccount                    | False<br>PaymentPartyRole     |
| CreditTransferTransaction70 | Purpose                          | PaymentObligation              | False<br>PaymentObligation    |
| CreditTransferTransaction70 | RegulatoryReporting              | RegulatoryReport               | False<br>FinancialTransaction |
| CreditTransferTransaction70 | RelatedRemittanceInformation     | ContactPoint                   | False<br>PaymentObligation    |
| CreditTransferTransaction70 | RemittanceInformation            | Document                       | False<br>PaymentObligation    |
| CreditTransferTransaction70 | SettlementPriority               |                                | False<br>PaymentProcessing    |
| CreditTransferTransaction70 | SettlementTimeIndication         | CashSettlement                 | False<br>PaymentInstruction   |
| CreditTransferTransaction70 | SettlementTimeRequest            | SettlementTimeRequest          | False<br>Payment              |
| CreditTransferTransaction70 | SupplementaryData                |                                | True                          |
| CreditTransferTransaction70 | Tax                              | Tax                            | False<br>Payment              |
| CreditTransferTransaction70 | UltimateCreditor                 | PartyIdentificationInformation | False<br>Party                |
| CreditTransferTransaction70 | UltimateDebtor                   | PartyIdentificationInformation | False<br>Party                |
| CryptographicKey1Choice     |                                  |                                | True                          |
| CryptographicKey1Choice     | ILPV4                            |                                | True                          |
| CryptographicKey1Choice     | Signature                        |                                | True                          |
| CurrencyExchange26          |                                  |                                | False<br>CurrencyExchange     |
| CurrencyExchange26          | ForeignExchangeAgent             | Organisation                   | False<br>CurrencyExchange     |
|                             |                                  |                                |                               |

| CurrencyExchange26     | PreAgreedExchangeRate | False | CurrencyExchange   |
|------------------------|-----------------------|-------|--------------------|
| CurrencyExchange26     | QuotationDateTime     | False | CurrencyExchange   |
| CurrencyExchange26     | QuotedCurrency        | False | CurrencyExchange   |
| CurrencyExchange26     | QuoteIdentification   | False | CurrencyExchange   |
| CurrencyExchange26     | UnitCurrency          | False | CurrencyExchange   |
| DateAndDateTime2Choice |                       | True  |                    |
| DateAndDateTime2Choice | Date                  | True  |                    |
| DateAndDateTime2Choice | DateTime              | True  |                    |
| DateAndPlaceOfBirth1   |                       | False | Person             |
| DateAndPlaceOfBirth1   | BirthDate             | False | Person             |
| DateAndPlaceOfBirth1   | CityOfBirth           | False | PostalAddress      |
| DateAndPlaceOfBirth1   | CountryOfBirth        | False | Country            |
| DateAndPlaceOfBirth1   | ProvinceOfBirth       | False | CountrySubDivision |
| DateAndType1           |                       | True  |                    |
| DateAndType1           | Date                  | True  |                    |
| DateAndType1           | Type                  | True  |                    |
| DatePeriod2            |                       | True  |                    |
| DatePeriod2            | FromDate              | False | DateTimePeriod     |
| DatePeriod2            | ToDate                | False | DateTimePeriod     |
| DateType2Choice        |                       | True  |                    |

| DateType2Choice                     | Code                          |                                | True  |                  |
|-------------------------------------|-------------------------------|--------------------------------|-------|------------------|
| DateType2Choice                     | Proprietary                   |                                | True  |                  |
| DirectDebitTransaction12            |                               |                                | False | DirectDebit      |
| DirectDebitTransaction12            | CreditorSchemeIdentification  | PartyIdentificationInformation | False | Party            |
| DirectDebitTransaction12            | MandateRelatedInformation     | DirectDebitMandate             | False | DirectDebit      |
| DirectDebitTransaction12            | PreNotificationDate           |                                | False | DirectDebit      |
| DirectDebitTransaction12            | PreNotificationIdentification |                                | False | DirectDebit      |
| DirectDebitTransactionInformation31 |                               |                                | False | DirectDebit      |
| DirectDebitTransactionInformation31 | ChargeBearer                  |                                | False | Charges          |
| DirectDebitTransactionInformation31 | ChargesInformation            | Charges                        | False |                  |
| DirectDebitTransactionInformation31 | Creditor                      | PartyIdentificationInformation | False | Party            |
| DirectDebitTransactionInformation31 | CreditorAccount               | CashAccount                    | False | PaymentPartyRole |
| DirectDebitTransactionInformation31 | CreditorAgent                 | Organisation                   | False | Organisation     |
| DirectDebitTransactionInformation31 | CreditorAgentAccount          | CashAccount                    | False | PaymentPartyRole |
| DirectDebitTransactionInformation31 | Debtor                        | PartyIdentificationInformation | False | Party            |
| DirectDebitTransactionInformation31 | DebtorAccount                 | CashAccount                    | False | PaymentPartyRole |
| DirectDebitTransactionInformation31 | DebtorAgent                   | Organisation                   | False | Organisation     |
| DirectDebitTransactionInformation31 | DebtorAgentAccount            | CashAccount                    | False | PaymentPartyRole |

| DirectDebitTransactionInformation31 | DirectDebitTransaction    | DirectDebit                    | False |
|-------------------------------------|---------------------------|--------------------------------|-------|
| DirectDebitTransactionInformation31 | ExchangeRate              |                                | False |
| DirectDebitTransactionInformation31 | InitiatingParty           | PartyIdentificationInformation | False |
| DirectDebitTransactionInformation31 | InstructedAgent           | Organisation                   | False |
| DirectDebitTransactionInformation31 | InstructedAmount          |                                | False |
| DirectDebitTransactionInformation31 | InstructingAgent          | Organisation                   | False |
| DirectDebitTransactionInformation31 | InterbankSettlementAmount |                                | False |
| DirectDebitTransactionInformation31 | InterbankSettlementDate   |                                | False |
| DirectDebitTransactionInformation31 | IntermediaryAgent1        | Organisation                   | False |
| DirectDebitTransactionInformation31 | IntermediaryAgent1Account | CashAccount                    | False |
| DirectDebitTransactionInformation31 | IntermediaryAgent2        | Organisation                   | False |
| DirectDebitTransactionInformation31 | IntermediaryAgent2Account | CashAccount                    | False |
| DirectDebitTransactionInformation31 | IntermediaryAgent3        | Organisation                   | False |
| DirectDebitTransactionInformation31 | IntermediaryAgent3Account | CashAccount                    | False |
| DirectDebitTransactionInformation31 | PaymentIdentification     | PaymentIdentification          | False |
| DirectDebitTransactionInformation31 | PaymentTypeInformation    | PaymentProcessing              | False |

| DirectDebitTransactionInformation31 | Purpose                      | PaymentObligation              | False | PaymentProcessing    |
|-------------------------------------|------------------------------|--------------------------------|-------|----------------------|
| DirectDebitTransactionInformation31 | RegulatoryReporting          | RegulatoryReport               | False | FinancialTransaction |
| DirectDebitTransactionInformation31 | RelatedRemittanceInformation | ContactPoint                   | False | Document             |
| DirectDebitTransactionInformation31 | RemittanceInformation        | Document                       | False | PaymentObligation    |
| DirectDebitTransactionInformation31 | RequestedCollectionDate      |                                | False | Obligation           |
| DirectDebitTransactionInformation31 | SettlementPriority           |                                | False | PaymentProcessing    |
| DirectDebitTransactionInformation31 | SettlementTimeIndication     | CashSettlement                 | False | PaymentInstruction   |
| DirectDebitTransactionInformation31 | SupplementaryData            |                                | True  |                      |
| DirectDebitTransactionInformation31 | UltimateCreditor             | PartyIdentificationInformation | False | Party                |
| DirectDebitTransactionInformation31 | UltimateDebtor               | PartyIdentificationInformation | False | Party                |
| DirectDebitTransactionInformation33 |                              |                                | False | DirectDebit          |
| DirectDebitTransactionInformation33 | Debtor                       | Organisation                   | False | Party                |
| DirectDebitTransactionInformation33 | DebtorAccount                | CashAccount                    | False | PaymentPartyRole     |
| DirectDebitTransactionInformation33 | DebtorAgent                  | Organisation                   | False | Organisation         |
| DirectDebitTransactionInformation33 | DebtorAgentAccount           | CashAccount                    | False | PaymentPartyRole     |
| DirectDebitTransactionInformation33 | InstructionForDebtorAgent    |                                | False | Payment              |
| DirectDebitTransactionInformation33 | InterbankSettlementAmount    |                                | False | CashSettlement       |

| DirectDebitTransactionInformation33 | InterbankSettlementDate  |                       | False<br>CashSettlement     |
|-------------------------------------|--------------------------|-----------------------|-----------------------------|
| DirectDebitTransactionInformation33 | PaymentIdentification    | PaymentIdentification | False<br>Payment            |
| DirectDebitTransactionInformation33 | PaymentTypeInformation   | PaymentProcessing     | False<br>Payment            |
| DirectDebitTransactionInformation33 | Purpose                  | PaymentObligation     | False<br>PaymentProcessing  |
| DirectDebitTransactionInformation33 | RemittanceInformation    | Document              | False<br>PaymentObligation  |
| DirectDebitTransactionInformation33 | SettlementPriority       |                       | False<br>PaymentProcessing  |
| DirectDebitTransactionInformation33 | SettlementTimeIndication | CashSettlement        | False<br>PaymentInstruction |
| DirectDebitTransactionInformation33 | SettlementTimeRequest    | SettlementTimeRequest | False<br>Payment            |
| DirectDebitTransactionInformation33 | UltimateDebtor           | Organisation          | False<br>Party              |
| DocumentAdjustment1                 |                          |                       | False<br>Adjustment         |
| DocumentAdjustment1                 | AdditionalInformation    |                       | True                        |
| DocumentAdjustment1                 | Amount                   |                       | False<br>Adjustment         |
| DocumentAdjustment1                 | CreditDebitIndicator     |                       | False<br>Adjustment         |
| DocumentAdjustment1                 | Reason                   |                       | False<br>Adjustment         |
| DocumentAmount1                     |                          |                       | False<br>Adjustment         |
| DocumentAmount1                     | Amount                   |                       | False<br>Adjustment         |
| DocumentAmount1                     | Type                     | Discount              | False                       |
| DocumentAmountType1Choice           |                          |                       | False<br>Discount           |

| DocumentAmountType1Choice   | Code              |          | False | Discount              |
|-----------------------------|-------------------|----------|-------|-----------------------|
| DocumentAmountType1Choice   | Proprietary       |          | True  |                       |
| DocumentLineIdentification1 |                   |          | False | Document              |
| DocumentLineIdentification1 | Number            |          | True  |                       |
| DocumentLineIdentification1 | RelatedDate       |          | False | Document              |
| DocumentLineIdentification1 | Type              | Document | False | Document              |
| DocumentLineInformation2    |                   |          | False | Document              |
| DocumentLineInformation2    | Amount            | Document | False | Document              |
| DocumentLineInformation2    | Description       |          | False |                       |
| DocumentLineInformation2    | Identification    | Document | False | GenericIdentification |
| DocumentLineType1           |                   |          | False | Document              |
| DocumentLineType1           | CodeOrProprietary | Document | False |                       |
| DocumentLineType1           | Issuer            |          | False | GenericIdentification |
| DocumentLineType1Choice     |                   |          | False | Document              |
| DocumentLineType1Choice     | Code              |          | False | Document              |
| DocumentLineType1Choice     | Proprietary       |          | False | Document              |
| DocumentType1               |                   |          | False | Document              |
| DocumentType1               | CodeOrProprietary | Document | False |                       |
| DocumentType1               | Issuer            |          | False |                       |

| DocumentType2Choice                      |                                    |                            | False | Document                   |
|------------------------------------------|------------------------------------|----------------------------|-------|----------------------------|
| DocumentType2Choice                      | Code                               |                            | False | Document                   |
| DocumentType2Choice                      | Proprietary                        |                            | False | Document                   |
| EquivalentAmount2                        |                                    |                            | False | Payment                    |
| EquivalentAmount2                        | Amount                             |                            | False | Payment                    |
| EquivalentAmount2                        | CurrencyOfTransfer                 |                            | False | Payment                    |
| FinancialIdentificationSchemeName1Choice |                                    |                            | False | Scheme                     |
| FinancialIdentificationSchemeName1Choice | Code                               |                            | False | Scheme                     |
| FinancialIdentificationSchemeName1Choice | Proprietary                        |                            | False | Scheme                     |
| FinancialInstitutionIdentification23     |                                    |                            | False | OrganisationIdentification |
| FinancialInstitutionIdentification23     | BICFI                              |                            | False | OrganisationIdentification |
| FinancialInstitutionIdentification23     | ClearingSystemMemberIdentification | CashClearingSystemMember   | False | OrganisationIdentification |
| FinancialInstitutionIdentification23     | LEI                                |                            | True  |                            |
| FinancialInstitutionIdentification23     | Name                               |                            | False | PartyName                  |
| FinancialInstitutionIdentification23     | Other                              | OrganisationIdentification | False |                            |
| FinancialInstitutionIdentification23     | PostalAddress                      | PostalAddress              | False |                            |
| Frequency36Choice                        |                                    |                            | True  |                            |
| Frequency36Choice                        | Period                             |                            | True  |                            |
| Frequency36Choice                        | PointInTime                        |                            | True  |                            |
| Frequency36Choice                        | Type                               |                            | True  |                            |

| FrequencyAndMoment1 |                                 |                                | True  |                   |
|---------------------|---------------------------------|--------------------------------|-------|-------------------|
| FrequencyAndMoment1 | PointInTime                     |                                | True  |                   |
| FrequencyAndMoment1 | Type                            |                                | True  |                   |
| FrequencyPeriod1    |                                 |                                | True  |                   |
| FrequencyPeriod1    | CountPerPeriod                  |                                | True  |                   |
| FrequencyPeriod1    | Type                            |                                | True  |                   |
| Garnishment4        |                                 |                                | False | Garnishment       |
| Garnishment4        | Date                            |                                | False | Trade             |
| Garnishment4        | EmployeeTerminationIndicator    |                                | False | PersonProfile     |
| Garnishment4        | FamilyMedicalInsuranceIndicator |                                | False | PersonProfile     |
| Garnishment4        | Garnishee                       | PartyIdentificationInformation | False |                   |
| Garnishment4        | GarnishmentAdministrator        | PartyIdentificationInformation | False | Party             |
| Garnishment4        | ReferenceNumber                 |                                | False | Tax               |
| Garnishment4        | RemittedAmount                  |                                | False | Document          |
| Garnishment4        | Type                            | Document                       | False | PaymentObligation |
| GarnishmentType1    |                                 |                                | False | Document          |
| GarnishmentType1    | CodeOrProprietary               | Document                       | False |                   |
| GarnishmentType1    | Issuer                          |                                | False |                   |

| GarnishmentType1Choice             |                |        | False |        | Document                   |                |
|------------------------------------|----------------|--------|-------|--------|----------------------------|----------------|
| GarnishmentType1Choice             | Code           |        | False |        | Document                   | Type           |
| GarnishmentType1Choice             | Proprietary    |        | False |        | Document                   | Type           |
| GenericAccountIdentification1      |                |        | False |        | AccountIdentification      |                |
| GenericAccountIdentification1      | Identification |        | False |        | GenericIdentification      | Identification |
| GenericAccountIdentification1      | Issuer         |        | False |        |                            |                |
| GenericAccountIdentification1      | SchemeName     | Scheme | False |        | GenericIdentification      | Scheme         |
| GenericFinancialIdentification1    |                |        | False |        | OrganisationIdentification |                |
| GenericFinancialIdentification1    | Identification |        | False |        | GenericIdentification      | Identification |
| GenericFinancialIdentification1    | Issuer         |        | False |        |                            |                |
| GenericFinancialIdentification1    | SchemeName     | Scheme | False |        | GenericIdentification      | Scheme         |
| GenericIdentification3             |                |        | False |        | GenericIdentification      |                |
| GenericIdentification3             | Identification |        | False |        | GenericIdentification      | Identification |
| GenericIdentification3             | Issuer         |        | False |        |                            |                |
| GenericIdentification30            |                |        | False |        | GenericIdentification      |                |
| GenericIdentification30            | Identification |        | False |        | GenericIdentification      | Identification |
| GenericIdentification30            | Issuer         |        | False |        |                            |                |
| GenericIdentification30            | SchemeName     |        | False | Scheme |                            | NameShort      |
| GenericOrganisationIdentification3 |                |        | False |        | OrganisationIdentification |                |

| GenericOrganisationIdentification3 | Identification        |                            | False |
|------------------------------------|-----------------------|----------------------------|-------|
| GenericOrganisationIdentification3 | Issuer                |                            | False |
| GenericOrganisationIdentification3 | SchemeName            | OrganisationIdentification | False |
| GenericPersonIdentification2       |                       |                            | False |
| GenericPersonIdentification2       | Identification        |                            | False |
| GenericPersonIdentification2       | Issuer                |                            | False |
| GenericPersonIdentification2       | SchemeName            | PersonIdentification       | False |
| GroupHeader109                     |                       |                            | False |
| GroupHeader109                     | CreationDateTime      |                            | False |
| GroupHeader109                     | InstructedAgent       | Organisation               | False |
| GroupHeader109                     | InstructingAgent      | Organisation               | False |
| GroupHeader109                     | MessageIdentification |                            | False |
| GroupHeader119                     |                       |                            | False |
| GroupHeader119                     | ControlSum            |                            | True  |
| GroupHeader119                     | CreationDateTime      |                            | False |
| GroupHeader119                     | InstructedAgent       | Organisation               | False |
| GroupHeader119                     | InstructingAgent      | Organisation               | False |
|                                    |                       |                            |       |

| GroupHeader119 | MessageIdentification   |              | False | PaymentIdentification |
|----------------|-------------------------|--------------|-------|-----------------------|
| GroupHeader119 | NumberOfTransactions    |              | True  |                       |
| GroupHeader120 |                         |              | False | Payment               |
| GroupHeader120 | CreationDateTime        |              | False |                       |
| GroupHeader120 | InstructedAgent         | Organisation | False |                       |
| GroupHeader120 | InstructingAgent        | Organisation | False |                       |
| GroupHeader120 | MessageIdentification   |              | False | PaymentIdentification |
| GroupHeader120 | OriginalBusinessQuery   |              | True  |                       |
| GroupHeader123 |                         |              | False | Payment               |
| GroupHeader123 | Authorisation           |              | True  |                       |
| GroupHeader123 | BatchBooking            |              | True  |                       |
| GroupHeader123 | ControlSum              |              | True  |                       |
| GroupHeader123 | CreationDateTime        |              | False | PaymentExecution      |
| GroupHeader123 | GroupReturn             |              | True  |                       |
| GroupHeader123 | InstructedAgent         | Organisation | False | Organisation          |
| GroupHeader123 | InstructingAgent        | Organisation | False | Organisation          |
| GroupHeader123 | InterbankSettlementDate |              | False |                       |
| GroupHeader123 | MessageIdentification   |              | False | PaymentIdentification |

| GroupHeader123 | NumberOfTransactions                   |                   | True  |                       |
|----------------|----------------------------------------|-------------------|-------|-----------------------|
| GroupHeader123 | PaymentTypeInformation                 | PaymentProcessing | False | PaymentExecution      |
| GroupHeader123 | SettlementInformation                  | CashSettlement    | False | PaymentInstruction    |
| GroupHeader123 | TotalReturnedInterbankSettlementAmount |                   | False | CashSettlement        |
| GroupHeader125 |                                        |                   | False | Payment               |
| GroupHeader125 | Authorisation                          |                   | True  |                       |
| GroupHeader125 | BatchBooking                           |                   | True  |                       |
| GroupHeader125 | ControlSum                             |                   | True  |                       |
| GroupHeader125 | CreationDateTime                       |                   | False |                       |
| GroupHeader125 | InstructedAgent                        | Organisation      | False | Organisation          |
| GroupHeader125 | InstructingAgent                       | Organisation      | False |                       |
| GroupHeader125 | InterbankSettlementDate                |                   | False |                       |
| GroupHeader125 | MessageIdentification                  |                   | False | PaymentIdentification |
| GroupHeader125 | NumberOfTransactions                   |                   | True  |                       |
| GroupHeader125 | PaymentTypeInformation                 | PaymentProcessing | False | PaymentExecution      |
| GroupHeader125 | SettlementInformation                  | CashSettlement    | False |                       |
| GroupHeader125 | TotalInterbankSettlementAmount         |                   | False |                       |
|                |                                        |                   |       |                       |

| GroupHeader127 |                                        |                | False | Payment               |
|----------------|----------------------------------------|----------------|-------|-----------------------|
| GroupHeader127 | Authorisation                          |                | True  |                       |
| GroupHeader127 | BatchBooking                           |                | True  |                       |
| GroupHeader127 | ControlSum                             |                | True  |                       |
| GroupHeader127 | CreationDateTime                       |                | False | PaymentExecution      |
| GroupHeader127 | GroupReversal                          |                | True  |                       |
| GroupHeader127 | InstructedAgent                        | Organisation   | False | Organisation          |
| GroupHeader127 | InstructingAgent                       | Organisation   | False | Organisation          |
| GroupHeader127 | InterbankSettlementDate                |                | False |                       |
| GroupHeader127 | MessageIdentification                  |                | False | PaymentIdentification |
| GroupHeader127 | NumberOfTransactions                   |                | True  |                       |
| GroupHeader127 | SettlementInformation                  | CashSettlement | False |                       |
| GroupHeader127 | TotalReversedInterbankSettlementAmount |                | False |                       |
| GroupHeader131 |                                        |                | False | Payment               |
| GroupHeader131 | BatchBooking                           |                | True  |                       |
| GroupHeader131 | ControlSum                             |                | True  |                       |
| GroupHeader131 | CreationDateTime                       |                | False |                       |
| GroupHeader131 | ExpiryDateTime                         |                | False |                       |

| GroupHeader131               | InstructedAgent                | Organisation      | False | Organisation          |
|------------------------------|--------------------------------|-------------------|-------|-----------------------|
| GroupHeader131               | InstructingAgent               | Organisation      | False | Organisation          |
| GroupHeader131               | InterbankSettlementDate        |                   | False | CashSettlement        |
| GroupHeader131               | MessageIdentification          |                   | False | PaymentIdentification |
| GroupHeader131               | NumberOfTransactions           |                   | True  |                       |
| GroupHeader131               | PaymentTypeInformation         | PaymentProcessing | False | PaymentExecution      |
| GroupHeader131               | SettlementInformation          | CashSettlement    | False | PaymentInstruction    |
| GroupHeader131               | TotalInterbankSettlementAmount |                   | False | CashSettlement        |
| InstructionForCreditorAgent3 |                                |                   | False |                       |
| InstructionForCreditorAgent3 | Code                           |                   | False |                       |
| InstructionForCreditorAgent3 | InstructionInformation         |                   | True  |                       |
| InstructionForNextAgent1     |                                |                   | False |                       |
| InstructionForNextAgent1     | Code                           |                   | False |                       |
| InstructionForNextAgent1     | InstructionInformation         |                   | True  |                       |
| LocalInstrument2Choice       |                                |                   | False |                       |
| LocalInstrument2Choice       | Code                           |                   | False |                       |
| LocalInstrument2Choice       | Proprietary                    |                   | False |                       |
| MandateClassification1Choice |                                |                   | False |                       |

| MandateClassification1Choice | Code                        |                       | False | PaymentProcessing  |
|------------------------------|-----------------------------|-----------------------|-------|--------------------|
| MandateClassification1Choice | Proprietary                 |                       | False | PaymentProcessing  |
| MandateRelatedData3Choice    |                             |                       | True  |                    |
| MandateRelatedData3Choice    | CreditTransferMandate       | CreditTransferMandate | True  |                    |
| MandateRelatedData3Choice    | DirectDebitMandate          | DirectDebitMandate    | True  |                    |
| MandateRelatedInformation16  |                             |                       | False | DirectDebitMandate |
| MandateRelatedInformation16  | AmendmentIndicator          |                       | False | Mandate            |
| MandateRelatedInformation16  | AmendmentInformationDetails | DirectDebitMandate    | False |                    |
| MandateRelatedInformation16  | DateOfSignature             |                       | False | Agreement          |
| MandateRelatedInformation16  | ElectronicSignature         |                       | False |                    |
| MandateRelatedInformation16  | FinalCollectionDate         |                       | False | DirectDebitMandate |
| MandateRelatedInformation16  | FirstCollectionDate         |                       | False | DirectDebitMandate |
| MandateRelatedInformation16  | Frequency                   |                       | False | Mandate            |
| MandateRelatedInformation16  | MandateIdentification       |                       | False | Mandate            |
| MandateRelatedInformation16  | Reason                      |                       | False | Agreement          |
| MandateRelatedInformation16  | TrackingDays                |                       | False | Mandate            |
| MandateSetupReason1Choice    |                             |                       | True  |                    |
| MandateSetupReason1Choice    | Code                        |                       | True  |                    |
| MandateSetupReason1Choice    | Proprietary                 |                       | True  |                    |

| MandateTypeInformation2                     |                              |                            | False | Mandate                        |
|---------------------------------------------|------------------------------|----------------------------|-------|--------------------------------|
| MandateTypeInformation2                     | CategoryPurpose              | Payment                    | False | PaymentProcessing              |
| MandateTypeInformation2                     | Classification               | Payment                    | False | DirectDebitMandate             |
| MandateTypeInformation2                     | LocalInstrument              | PaymentProcessing          | False | Mandate                        |
| MandateTypeInformation2                     | ServiceLevel                 | ServiceLevel               | False | PaymentProcessing              |
| NameAndAddress18                            |                              |                            | False | PartyIdentificationInformation |
| NameAndAddress18                            | Address                      | PostalAddress              | False |                                |
| NameAndAddress18                            | Name                         |                            | False | PartyName                      |
| NumberOfTransactionsPerStatus5              |                              |                            | True  |                                |
| NumberOfTransactionsPerStatus5              | DetailedControlSum           |                            | True  |                                |
| NumberOfTransactionsPerStatus5              | DetailedNumberOfTransactions |                            | True  |                                |
| NumberOfTransactionsPerStatus5              | DetailedStatus               |                            | True  |                                |
| OrganisationIdentification39                |                              |                            | False | OrganisationIdentification     |
| OrganisationIdentification39                | AnyBIC                       |                            | False | OrganisationIdentification     |
| OrganisationIdentification39                | LEI                          |                            | True  |                                |
| OrganisationIdentification39                | Other                        | OrganisationIdentification | False | PartyIdentificationInformation |
| OrganisationIdentificationSchemeName1Choice |                              |                            | False | OrganisationIdentification     |
| OrganisationIdentificationSchemeName1Choice | Code                         |                            | False | Scheme                         |
| OrganisationIdentificationSchemeName1Choice | Proprietary                  |                            | False | Scheme                         |

| OriginalBusinessQuery1 |                                           | True  |                       |
|------------------------|-------------------------------------------|-------|-----------------------|
|                        |                                           |       |                       |
| OriginalBusinessQuery1 | CreationDateTime                          | True  |                       |
| OriginalBusinessQuery1 | MessageIdentification                     | True  |                       |
| OriginalBusinessQuery1 | MessageNameIdentification                 | True  |                       |
| OriginalGroupHeader19  |                                           | False | PaymentExecution      |
| OriginalGroupHeader19  | OriginalCreationDateTime                  | False | PaymentExecution      |
| OriginalGroupHeader19  | OriginalMessageIdentification             | False | PaymentIdentification |
| OriginalGroupHeader19  | OriginalMessageNameIdentification         | True  |                       |
| OriginalGroupHeader19  | ReturnReasonInformation<br>StatusReason   | False | Status                |
| OriginalGroupHeader20  |                                           | False | PaymentExecution      |
| OriginalGroupHeader20  | OriginalCreationDateTime                  | False | PaymentExecution      |
| OriginalGroupHeader20  | OriginalMessageIdentification             | False | PaymentIdentification |
| OriginalGroupHeader20  | OriginalMessageNameIdentification         | True  |                       |
| OriginalGroupHeader20  | ReversalReasonInformation<br>StatusReason | False | Payment               |
| OriginalGroupHeader22  |                                           | False | PaymentExecution      |
| OriginalGroupHeader22  | GroupStatus                               | False | PaymentStatus         |
| OriginalGroupHeader22  | NumberOfTransactionsPerStatus             | True  |                       |
| OriginalGroupHeader22  | OriginalControlSum                        | True  |                       |
| OriginalGroupHeader22  | OriginalCreationDateTime                  | False | PaymentExecution      |

| OriginalGroupHeader22          | OriginalMessageIdentification     |                                | False |
|--------------------------------|-----------------------------------|--------------------------------|-------|
| OriginalGroupHeader22          | OriginalMessageNameIdentification |                                | True  |
| OriginalGroupHeader22          | OriginalNumberOfTransactions      |                                | True  |
| OriginalGroupHeader22          | StatusReasonInformation           | PaymentStatus                  | False |
| OriginalGroupInformation27     |                                   |                                | False |
| OriginalGroupInformation27     | OriginalControlSum                |                                | True  |
| OriginalGroupInformation27     | OriginalCreationDateTime          |                                | False |
| OriginalGroupInformation27     | OriginalMessageIdentification     |                                | False |
| OriginalGroupInformation27     | OriginalMessageNameIdentification |                                | True  |
| OriginalGroupInformation27     | OriginalNumberOfTransactions      |                                | True  |
| OriginalGroupInformation29     |                                   |                                | False |
| OriginalGroupInformation29     | OriginalCreationDateTime          |                                | False |
| OriginalGroupInformation29     | OriginalMessageIdentification     |                                | False |
| OriginalGroupInformation29     | OriginalMessageNameIdentification |                                | True  |
| OriginalTransactionReference42 |                                   |                                | False |
| OriginalTransactionReference42 | Amount                            | Payment                        | False |
| OriginalTransactionReference42 | Creditor                          | PartyIdentificationInformation | False |
| OriginalTransactionReference42 | CreditorAccount                   | CashAccount                    | False |
| OriginalTransactionReference42 | CreditorAgent                     | Organisation                   | False |
|                                |                                   |                                |       |

| OriginalTransactionReference42 | CreditorAgentAccount         | CashAccount                    | False | PaymentPartyRole   |
|--------------------------------|------------------------------|--------------------------------|-------|--------------------|
| OriginalTransactionReference42 | CreditorSchemeIdentification | PartyIdentificationInformation | False | Party              |
| OriginalTransactionReference42 | Debtor                       | PartyIdentificationInformation | False | Party              |
| OriginalTransactionReference42 | DebtorAccount                | CashAccount                    | False | PaymentPartyRole   |
| OriginalTransactionReference42 | DebtorAgent                  | Organisation                   | False | Party              |
| OriginalTransactionReference42 | DebtorAgentAccount           | CashAccount                    | False | PaymentPartyRole   |
| OriginalTransactionReference42 | InterbankSettlementAmount    |                                | False | CashSettlement     |
| OriginalTransactionReference42 | InterbankSettlementDate      |                                | False | CashSettlement     |
| OriginalTransactionReference42 | MandateRelatedInformation    |                                | False |                    |
| OriginalTransactionReference42 | PaymentMethod                |                                | False | CreditInstrument   |
| OriginalTransactionReference42 | PaymentTypeInformation       | PaymentProcessing              | False | PaymentExecution   |
| OriginalTransactionReference42 | Purpose                      | PaymentObligation              | False | PaymentObligation  |
| OriginalTransactionReference42 | RemittanceInformation        | Document                       | False | PaymentObligation  |
| OriginalTransactionReference42 | RequestedCollectionDate      |                                | False | Obligation         |
| OriginalTransactionReference42 | RequestedExecutionDate       |                                | False | Obligation         |
| OriginalTransactionReference42 | SettlementInformation        | CashSettlement                 | False | PaymentInstruction |
| OriginalTransactionReference42 | UltimateCreditor             | PartyIdentificationInformation | False |                    |

| OriginalTransactionReference42 | UltimateDebtor               | PartyIdentificationInformation | False | Party                     |
|--------------------------------|------------------------------|--------------------------------|-------|---------------------------|
| OriginalTransactionReference44 |                              |                                | False | Payment                   |
| OriginalTransactionReference44 | Amount                       | Payment                        | False | Payment                   |
| OriginalTransactionReference44 | Creditor                     | PartyIdentificationInformation | False | Party                     |
| OriginalTransactionReference44 | CreditorAccount              | CashAccount                    | False | PaymentPartyRole          |
| OriginalTransactionReference44 | CreditorAgent                | Organisation                   | False | Party                     |
| OriginalTransactionReference44 | CreditorAgentAccount         | CashAccount                    | False | PaymentPartyRole          |
| OriginalTransactionReference44 | CreditorSchemeIdentification | PartyIdentificationInformation | False | Party                     |
| OriginalTransactionReference44 | Debtor                       | PartyIdentificationInformation | False | Party                     |
|                                |                              |                                |       |                           |
| OriginalTransactionReference44 | DebtorAccount                | CashAccount                    | False |                           |
| OriginalTransactionReference44 | DebtorAgent                  | Organisation                   | False | PaymentPartyRole<br>Party |
| OriginalTransactionReference44 | DebtorAgentAccount           | CashAccount                    | False | PaymentPartyRole          |
| OriginalTransactionReference44 | InterbankSettlementAmount    |                                | False | CashSettlement            |
| OriginalTransactionReference44 | InterbankSettlementDate      |                                | False |                           |
| OriginalTransactionReference44 | MandateRelatedInformation    |                                | False |                           |

| OriginalTransactionReference44 | PaymentTypeInformation                       | PaymentProcessing              | False | PaymentExecution               |
|--------------------------------|----------------------------------------------|--------------------------------|-------|--------------------------------|
| OriginalTransactionReference44 | Purpose                                      | PaymentObligation              | False | PaymentObligation              |
| OriginalTransactionReference44 | RemittanceInformation                        | Document                       | False | PaymentObligation              |
| OriginalTransactionReference44 | RequestedCollectionDate                      |                                | False | Obligation                     |
| OriginalTransactionReference44 | RequestedExecutionDate                       |                                | False |                                |
| OriginalTransactionReference44 | SettlementInformation                        | CashSettlement                 | False | PaymentInstruction             |
| OriginalTransactionReference44 | UltimateCreditor                             | PartyIdentificationInformation | False | Party                          |
| OriginalTransactionReference44 | UltimateDebtor                               | PartyIdentificationInformation | False |                                |
| OriginalTransactionReference44 | UnderlyingCustomerCreditTransfer             | CreditTransfer                 | False |                                |
| OriginalTransactionReference44 | UnderlyingFinancialInstitutionCreditTransfer | CreditTransfer                 | False |                                |
| OtherContact1                  |                                              |                                | False |                                |
| OtherContact1                  | ChannelType                                  |                                | True  |                                |
| OtherContact1                  | Identification                               |                                | False | ContactPoint                   |
| Party50Choice                  |                                              |                                | False | PartyIdentificationInformation |
| Party50Choice                  | Agent                                        | Organisation                   | False |                                |
| Party50Choice                  | Party                                        | PartyIdentificationInformation | False |                                |
| Party52Choice                  |                                              |                                | False |                                |
| Party52Choice                  | OrganisationIdentification                   | OrganisationIdentification     | False |                                |
| Party52Choice                  | PrivateIdentification                        | PersonIdentification           | False |                                |

| PartyIdentification272  |                           |                                | False | PartyIdentificationInformation |
|-------------------------|---------------------------|--------------------------------|-------|--------------------------------|
| PartyIdentification272  | ContactDetails            | PersonIdentification           | False | Party                          |
| PartyIdentification272  | CountryOfResidence        |                                | False | Country                        |
| PartyIdentification272  | Identification            | PartyIdentificationInformation | False |                                |
| PartyIdentification272  | Name                      |                                | False | PartyName                      |
| PartyIdentification272  | PostalAddress             | PostalAddress                  | False |                                |
| PaymentIdentification13 |                           |                                | False | PaymentIdentification          |
| PaymentIdentification13 | ClearingSystemReference   |                                | False | PaymentIdentification          |
| PaymentIdentification13 | EndToEndIdentification    |                                | False | PaymentIdentification          |
| PaymentIdentification13 | InstructionIdentification |                                | False | PaymentIdentification          |
| PaymentIdentification13 | TransactionIdentification |                                | False | PaymentIdentification          |
| PaymentIdentification13 | UETR                      |                                | False | PaymentIdentification          |
| PaymentReturnReason7    |                           |                                | False | StatusReason                   |
| PaymentReturnReason7    | AdditionalInformation     |                                | True  |                                |
| PaymentReturnReason7    | Originator                | PartyIdentificationInformation | False |                                |
| PaymentReturnReason7    | Reason                    | StatusReason                   | False |                                |
| PaymentReversalReason10 |                           |                                | False | StatusReason                   |
| PaymentReversalReason10 | AdditionalInformation     |                                | False | StatusReason                   |
| PaymentReversalReason10 | Originator                | PartyIdentificationInformation | False | Party                          |
|                         |                           |                                |       |                                |

| PaymentReversalReason10 | Reason                            | PaymentStatus | False                          |
|-------------------------|-----------------------------------|---------------|--------------------------------|
| PaymentTransaction149   |                                   |               | False<br>Payment               |
| PaymentTransaction149   | ChargeBearer                      |               | False<br>Charges               |
| PaymentTransaction149   | ChargesInformation                | Charges       | False                          |
| PaymentTransaction149   | CompensationAmount                |               | False<br>Adjustment            |
| PaymentTransaction149   | ExchangeRate                      |               | False<br>CurrencyExchange      |
| PaymentTransaction149   | InstructedAgent                   | Organisation  | False<br>Organisation          |
| PaymentTransaction149   | InstructingAgent                  | Organisation  | False<br>Organisation          |
| PaymentTransaction149   | InterbankSettlementDate           |               | False<br>CashSettlement        |
| PaymentTransaction149   | OriginalClearingSystemReference   |               | False<br>PaymentIdentification |
| PaymentTransaction149   | OriginalEndToEndIdentification    |               | False<br>PaymentIdentification |
| PaymentTransaction149   | OriginalGroupInformation          | Payment       | False<br>Payment               |
| PaymentTransaction149   | OriginalInstructionIdentification |               | False<br>PaymentIdentification |
| PaymentTransaction149   | OriginalInterbankSettlementAmount |               | False<br>CashSettlement        |
| PaymentTransaction149   | OriginalTransactionIdentification |               | False<br>PaymentIdentification |
| PaymentTransaction149   | OriginalTransactionReference      | Payment       | False                          |
| PaymentTransaction149   | OriginalUETR                      |               | False<br>PaymentIdentification |
| PaymentTransaction149   | ReversalIdentification            |               | True                           |

| PaymentTransaction149 | ReversalReasonInformation         | StatusReason   | False<br>Status                |
|-----------------------|-----------------------------------|----------------|--------------------------------|
| PaymentTransaction149 | ReversedInstructedAmount          |                | False<br>Payment               |
| PaymentTransaction149 | ReversedInterbankSettlementAmount |                | False<br>CashSettlement        |
| PaymentTransaction149 | SettlementPriority                |                | False<br>PaymentProcessing     |
| PaymentTransaction149 | SettlementTimeIndication          | CashSettlement | False<br>PaymentInstruction    |
| PaymentTransaction149 | SupplementaryData                 |                | True                           |
| PaymentTransaction158 |                                   |                | False<br>Payment               |
| PaymentTransaction158 | AcceptanceDateTime                |                | False<br>PaymentExecution      |
| PaymentTransaction158 | ClearingSystemReference           |                | False<br>PaymentIdentification |
| PaymentTransaction158 | InstructedAgent                   | Organisation   | False<br>Organisation          |
| PaymentTransaction158 | InstructingAgent                  | Organisation   | False<br>Organisation          |
| PaymentTransaction158 | OriginalEndToEndIdentification    |                | False<br>PaymentIdentification |
| PaymentTransaction158 | OriginalGroupInformation          | Payment        | False<br>PaymentExecution      |
| PaymentTransaction158 | OriginalInstructionIdentification |                | False<br>PaymentIdentification |
| PaymentTransaction158 | OriginalTransactionIdentification |                | False<br>PaymentIdentification |
| PaymentTransaction158 | OriginalTransactionReference      | Payment        | True                           |
| PaymentTransaction158 | OriginalUETR                      |                | False<br>PaymentIdentification |
| PaymentTransaction158 | StatusRequestIdentification       |                | True                           |

| PaymentTransaction158 | SupplementaryData                 |                  | True                           |
|-----------------------|-----------------------------------|------------------|--------------------------------|
| PaymentTransaction163 |                                   |                  | False<br>Payment               |
| PaymentTransaction163 | AgreedRate                        | CurrencyExchange | True                           |
| PaymentTransaction163 | ChargeBearer                      |                  | False<br>Charges               |
| PaymentTransaction163 | ChargesInformation                | Charges          | False                          |
| PaymentTransaction163 | ClearingSystemReference           |                  | False<br>PaymentIdentification |
| PaymentTransaction163 | CompensationAmount                |                  | False<br>Adjustment            |
| PaymentTransaction163 | ExchangeRate                      |                  | False<br>CurrencyExchange      |
| PaymentTransaction163 | InstructedAgent                   | Organisation     | False<br>Organisation          |
| PaymentTransaction163 | InstructingAgent                  | Organisation     | False<br>Organisation          |
| PaymentTransaction163 | InterbankSettlementDate           |                  | False<br>CashSettlement        |
| PaymentTransaction163 | OriginalClearingSystemReference   |                  | False<br>PaymentIdentification |
| PaymentTransaction163 | OriginalEndToEndIdentification    |                  | False<br>PaymentIdentification |
| PaymentTransaction163 | OriginalGroupInformation          | Payment          | False<br>Payment               |
| PaymentTransaction163 | OriginalInstructionIdentification |                  | False<br>PaymentIdentification |
| PaymentTransaction163 | OriginalInterbankSettlementAmount |                  | False<br>CashSettlement        |
| PaymentTransaction163 | OriginalInterbankSettlementDate   |                  | False<br>CashSettlement        |
| PaymentTransaction163 | OriginalTransactionIdentification |                  | False<br>PaymentIdentification |

| PaymentTransaction163 | OriginalTransactionReference      | Payment               | False                          |
|-----------------------|-----------------------------------|-----------------------|--------------------------------|
| PaymentTransaction163 | OriginalUETR                      |                       | False<br>PaymentIdentification |
| PaymentTransaction163 | PaymentTypeInformation            | PaymentProcessing     | False<br>PaymentExecution      |
| PaymentTransaction163 | ReturnChain                       | CreditTransfer        | False                          |
| PaymentTransaction163 | ReturnedInstructedAmount          |                       | False<br>Payment               |
| PaymentTransaction163 | ReturnedInterbankSettlementAmount |                       | False<br>CashSettlement        |
| PaymentTransaction163 | ReturnIdentification              |                       | True                           |
| PaymentTransaction163 | ReturnReasonInformation           | StatusReason          | False<br>Status                |
| PaymentTransaction163 | SettlementPriority                |                       | False<br>PaymentProcessing     |
| PaymentTransaction163 | SettlementTimeIndication          | CashSettlement        | False<br>PaymentInstruction    |
| PaymentTransaction163 | SettlementTimeRequest             | SettlementTimeRequest | False<br>Payment               |
| PaymentTransaction163 | SupplementaryData                 |                       | True                           |
| PaymentTransaction164 |                                   |                       | False<br>Payment               |
| PaymentTransaction164 | AcceptanceDateTime                |                       | False<br>PaymentExecution      |
| PaymentTransaction164 | AccountServicerReference          |                       | False<br>Entry                 |
| PaymentTransaction164 | ChargesInformation                | Charges               | False                          |
| PaymentTransaction164 | ClearingSystemReference           |                       | False<br>PaymentIdentification |
| PaymentTransaction164 | CreditSettlementKey               |                       | False<br>Status                |

| PaymentTransaction164    | EffectiveInterbankSettlementDate  |                   | False |
|--------------------------|-----------------------------------|-------------------|-------|
| PaymentTransaction164    | InstructedAgent                   | Organisation      | False |
| PaymentTransaction164    | InstructingAgent                  | Organisation      | False |
| PaymentTransaction164    | OriginalEndToEndIdentification    |                   | False |
| PaymentTransaction164    | OriginalGroupInformation          | Payment           | False |
| PaymentTransaction164    | OriginalInstructionIdentification |                   | False |
| PaymentTransaction164    | OriginalTransactionIdentification |                   | False |
| PaymentTransaction164    | OriginalTransactionReference      | Payment           | False |
| PaymentTransaction164    | OriginalUETR                      |                   | False |
| PaymentTransaction164    | ProcessingDate                    |                   | True  |
| PaymentTransaction164    | StatusIdentification              |                   | True  |
| PaymentTransaction164    | StatusReasonInformation           | PaymentStatus     | False |
| PaymentTransaction164    | SupplementaryData                 |                   | True  |
| PaymentTransaction164    | TransactionStatus                 |                   | False |
| PaymentTypeInformation27 |                                   |                   | False |
| PaymentTypeInformation27 | CategoryPurpose                   | Payment           | False |
| PaymentTypeInformation27 | ClearingChannel                   |                   | False |
| PaymentTypeInformation27 | InstructionPriority               |                   | False |
| PaymentTypeInformation27 | LocalInstrument                   | PaymentProcessing | False |

| PaymentTypeInformation27              | SequenceType        |                      | False<br>PaymentProcessing              |
|---------------------------------------|---------------------|----------------------|-----------------------------------------|
| PaymentTypeInformation27              | ServiceLevel        | ServiceLevel         | False<br>PaymentProcessing              |
| PaymentTypeInformation28              |                     |                      | False<br>PaymentProcessing              |
| PaymentTypeInformation28              | CategoryPurpose     | Payment              | False<br>PaymentProcessing              |
| PaymentTypeInformation28              | ClearingChannel     |                      | False<br>PaymentProcessing              |
| PaymentTypeInformation28              | InstructionPriority |                      | False<br>PaymentProcessing              |
| PaymentTypeInformation28              | LocalInstrument     | PaymentProcessing    | False<br>PaymentProcessing              |
| PaymentTypeInformation28              | ServiceLevel        | ServiceLevel         | False<br>PaymentProcessing              |
| PersonIdentification18                |                     |                      | False<br>PersonIdentification           |
| PersonIdentification18                | DateAndPlaceOfBirth | Person               | False<br>PersonIdentification           |
| PersonIdentification18                | Other               | PersonIdentification | False<br>PartyIdentificationInformation |
| PersonIdentificationSchemeName1Choice |                     |                      | False<br>PersonIdentification           |
| PersonIdentificationSchemeName1Choice | Code                |                      | False<br>Scheme                         |
| PersonIdentificationSchemeName1Choice | Proprietary         |                      | False<br>Scheme                         |
| PostalAddress27                       |                     |                      | False<br>PostalAddress                  |
| PostalAddress27                       | AddressLine         |                      | True                                    |
| PostalAddress27                       | AddressType         |                      | False<br>PostalAddress                  |
| PostalAddress27                       | BuildingName        |                      | False<br>PostalAddress                  |
| PostalAddress27                       | BuildingNumber      |                      | False<br>PostalAddress                  |
| PostalAddress27                       | CareOf              |                      | False<br>PostalAddress                  |
|                                       |                     |                      |                                         |

| PostalAddress27             | Country            |        | False | Country               |
|-----------------------------|--------------------|--------|-------|-----------------------|
| PostalAddress27             | CountrySubDivision |        | False | CountrySubDivision    |
| PostalAddress27             | Department         |        | False | PostalAddress         |
| PostalAddress27             | DistrictName       |        | False | CountrySubDivision    |
| PostalAddress27             | Floor              |        | False | PostalAddress         |
| PostalAddress27             | PostBox            |        | False | PostalAddress         |
| PostalAddress27             | PostCode           |        | False | PostalAddress         |
| PostalAddress27             | Room               |        | False | PostalAddress         |
| PostalAddress27             | StreetName         |        | False | PostalAddress         |
| PostalAddress27             | SubDepartment      |        | False | PostalAddress         |
| PostalAddress27             | TownLocationName   |        | False |                       |
| PostalAddress27             | TownName           |        | False | PostalAddress         |
| PostalAddress27             | UnitNumber         |        | False | PostalAddress         |
| ProxyAccountIdentification1 |                    |        | False | AccountIdentification |
| ProxyAccountIdentification1 | Identification     |        | False | GenericIdentification |
| ProxyAccountIdentification1 | Type               | Scheme | False | GenericIdentification |
| ProxyAccountType1Choice     |                    |        | False | Scheme                |
| ProxyAccountType1Choice     | Code               |        | False | Scheme                |
| ProxyAccountType1Choice     | Proprietary        |        | False | Scheme                |
| Purpose2Choice              |                    |        | False | PaymentObligation     |

| Purpose2Choice               | Code                                                      |          | False | PaymentObligation             |
|------------------------------|-----------------------------------------------------------|----------|-------|-------------------------------|
| Purpose2Choice               | Proprietary                                               |          | False | PaymentObligation             |
| References74Choice           |                                                           |          | False | SecuritiesTradeIdentification |
| References74Choice           | AccountServicerTransactionIdentification                  |          | False | Entry                         |
| References74Choice           | CommonIdentification                                      |          | False | TradeIdentification           |
| References74Choice           | CounterpartyMarketInfrastructureTransactionIdentification |          | False | SecuritiesTradeIdentification |
| References74Choice           | IntraBalanceMovementIdentification                        |          | True  |                               |
| References74Choice           | IntraPositionMovementIdentification                       |          | True  |                               |
| References74Choice           | MarketInfrastructureTransactionIdentification             |          | False | SecuritiesTradeIdentification |
| References74Choice           | OtherTransactionIdentification                            |          | False | TradeIdentification           |
| References74Choice           | PoolIdentification                                        |          | False | SecuritiesTradeIdentification |
| References74Choice           | SecuritiesSettlementTransactionIdentification             |          | False | SecuritiesTradeExecution      |
| References74Choice           | TradeIdentification                                       |          | False | TradeIdentification           |
| ReferredDocumentInformation8 |                                                           |          | False | Document                      |
| ReferredDocumentInformation8 | LineDetails                                               | Document | False |                               |
| ReferredDocumentInformation8 | Number                                                    |          | False | GenericIdentification         |
| ReferredDocumentInformation8 | RelatedDate                                               |          | False | Document                      |
| ReferredDocumentInformation8 | Type                                                      | Document | False | Document                      |
| RegulatoryAuthority2         |                                                           |          | False | RegulatoryAuthorityRole       |

| RegulatoryAuthority2    | Country                       |                         | False | Country          |
|-------------------------|-------------------------------|-------------------------|-------|------------------|
| RegulatoryAuthority2    | Name                          |                         | False | PartyName        |
| RegulatoryReporting3    |                               |                         | False | RegulatoryReport |
| RegulatoryReporting3    | Authority                     | RegulatoryAuthorityRole | False | RegulatoryReport |
| RegulatoryReporting3    | DebitCreditReportingIndicator |                         | False | RegulatoryReport |
| RegulatoryReporting3    | Details                       | RegulatoryReport        | False |                  |
| RemittanceAmount4       |                               |                         | False |                  |
| RemittanceAmount4       | AdjustmentAmountAndReason     | Adjustment              | False |                  |
| RemittanceAmount4       | RemittanceAmountAndType       | Adjustment              | False |                  |
| RemittanceInformation2  |                               |                         | False |                  |
| RemittanceInformation2  | Unstructured                  |                         | False |                  |
| RemittanceInformation22 |                               |                         | False |                  |
| RemittanceInformation22 | Structured                    | Document                | False |                  |
| RemittanceInformation22 | Unstructured                  |                         | False |                  |
| RemittanceLocation8     |                               |                         | False |                  |
| RemittanceLocation8     | RemittanceIdentification      |                         | True  |                  |
| RemittanceLocation8     | RemittanceLocationDetails     | ContactPoint            | False |                  |
| RemittanceLocationData2 |                               |                         | False |                  |
| RemittanceLocationData2 | ElectronicAddress             |                         | False |                  |
| RemittanceLocationData2 | Method                        |                         | False |                  |

| RemittanceLocationData2       | PostalAddress                | PartyIdentificationInformation | False |
|-------------------------------|------------------------------|--------------------------------|-------|
| ReturnReason5Choice           |                              |                                | False |
| ReturnReason5Choice           | Code                         |                                | False |
| ReturnReason5Choice           | Proprietary                  |                                | False |
| ReversalReason4Choice         |                              |                                | False |
| ReversalReason4Choice         | Code                         |                                | False |
| ReversalReason4Choice         | Proprietary                  |                                | False |
| ServiceLevel8Choice           |                              |                                | False |
| ServiceLevel8Choice           | Code                         |                                | False |
| ServiceLevel8Choice           | Proprietary                  |                                | False |
| SettlementDateTimeIndication1 |                              |                                | False |
| SettlementDateTimeIndication1 | CreditDateTime               |                                | False |
| SettlementDateTimeIndication1 | DebitDateTime                |                                | False |
| SettlementInstruction14       |                              |                                | False |
| SettlementInstruction14       | ClearingSystem               | CashClearingSystem             | False |
| SettlementInstruction14       | SettlementAccount            | CashAccount                    | False |
| SettlementInstruction14       | SettlementMethod             |                                | False |
| SettlementInstruction15       |                              |                                | False |
| SettlementInstruction15       | ClearingSystem               | CashClearingSystem             | False |
| SettlementInstruction15       | InstructedReimbursementAgent | Organisation                   | False |

| SettlementInstruction15   | InstructedReimbursementAgentAccount  | CashAccount                    | False | CashSettlementInstructionPartyRole |
|---------------------------|--------------------------------------|--------------------------------|-------|------------------------------------|
| SettlementInstruction15   | InstructingReimbursementAgent        | Organisation                   | False | Organisation                       |
| SettlementInstruction15   | InstructingReimbursementAgentAccount | CashAccount                    | False | CashSettlementInstructionPartyRole |
| SettlementInstruction15   | SettlementAccount                    | CashAccount                    | False | CashSettlement                     |
| SettlementInstruction15   | SettlementMethod                     |                                | False | CashSettlement                     |
| SettlementInstruction15   | ThirdReimbursementAgent              | Organisation                   | False | Party                              |
| SettlementInstruction15   | ThirdReimbursementAgentAccount       | CashAccount                    | False | CashSettlementInstructionPartyRole |
| SettlementTimeRequest2    |                                      |                                | False | SettlementTimeRequest              |
| SettlementTimeRequest2    | CLSTime                              |                                | False | SettlementTimeRequest              |
| SettlementTimeRequest2    | FromTime                             |                                | False | SettlementTimeRequest              |
| SettlementTimeRequest2    | RejectTime                           |                                | False | SettlementTimeRequest              |
| SettlementTimeRequest2    | TillTime                             |                                | False | SettlementTimeRequest              |
| StatusReason6Choice       |                                      |                                | False | StatusReason                       |
| StatusReason6Choice       | Code                                 |                                | False | StatusReason                       |
| StatusReason6Choice       | Proprietary                          |                                | False | StatusReason                       |
| StatusReasonInformation14 |                                      |                                | False | PaymentStatus                      |
| StatusReasonInformation14 | AdditionalInformation                |                                | False |                                    |
| StatusReasonInformation14 | Originator                           | PartyIdentificationInformation | False | Party                              |
|                           |                                      |                                |       |                                    |

| StatusReasonInformation14         | Reason                          | StatusReason                   | False | Status                |
|-----------------------------------|---------------------------------|--------------------------------|-------|-----------------------|
| StructuredRegulatoryReporting3    |                                 |                                | False | RegulatoryReport      |
| StructuredRegulatoryReporting3    | Amount                          |                                | False | RegulatoryReport      |
| StructuredRegulatoryReporting3    | Code                            |                                | False | RegulatoryReport      |
| StructuredRegulatoryReporting3    | Country                         |                                | False | Country               |
| StructuredRegulatoryReporting3    | Date                            |                                | False | RegulatoryReport      |
| StructuredRegulatoryReporting3    | Information                     |                                | False | RegulatoryReport      |
| StructuredRegulatoryReporting3    | Type                            |                                | False | RegulatoryReport      |
| StructuredRemittanceInformation18 |                                 |                                | False | Document              |
| StructuredRemittanceInformation18 | AdditionalRemittanceInformation |                                | False |                       |
| StructuredRemittanceInformation18 | CreditorReferenceInformation    | PaymentIdentification          | False | PaymentIdentification |
| StructuredRemittanceInformation18 | GarnishmentRemittance           | Garnishment                    | False |                       |
| StructuredRemittanceInformation18 | Invoicee                        | PartyIdentificationInformation | False |                       |
| StructuredRemittanceInformation18 | Invoicer                        | PartyIdentificationInformation | False | Party                 |
| StructuredRemittanceInformation18 | ReferredDocumentAmount          | Document                       | False | Document              |
| StructuredRemittanceInformation18 | ReferredDocumentInformation     | Document                       | False |                       |
| StructuredRemittanceInformation18 | TaxRemittance                   | Tax                            | False | Payment               |
| SupplementaryData1                |                                 |                                | True  |                       |
| SupplementaryData1                | Envelope                        |                                | True  |                       |

| SupplementaryData1 | PlaceAndName           |              | True  |              |
|--------------------|------------------------|--------------|-------|--------------|
| TaxAmount3         |                        |              | False | Tax          |
| TaxAmount3         | Details                | Tax          | True  |              |
| TaxAmount3         | Rate                   |              | False | Tax          |
| TaxAmount3         | TaxableBaseAmount      |              | False | Tax          |
| TaxAmount3         | TotalAmount            |              | False | Tax          |
| TaxAuthorisation1  |                        |              | False | TaxPartyRole |
| TaxAuthorisation1  | Name                   |              | False | PartyName    |
| TaxAuthorisation1  | Title                  |              | False | Person       |
| TaxData1           |                        |              | False | Tax          |
| TaxData1           | AdministrationZone     |              | False | Tax          |
| TaxData1           | Creditor               | TaxPartyRole | False |              |
| TaxData1           | Date                   |              | False | Tax          |
| TaxData1           | Debtor                 | TaxPartyRole | False |              |
| TaxData1           | Method                 |              | False | Tax          |
| TaxData1           | Record                 | TaxRecord    | False | Tax          |
| TaxData1           | ReferenceNumber        |              | False | Tax          |
| TaxData1           | SequenceNumber         |              | True  |              |
| TaxData1           | TotalTaxableBaseAmount |              | False | Tax          |
| TaxData1           | TotalTaxAmount         |              | False | Tax          |

| UltimateDebtor             | TaxPartyRole | False |
|----------------------------|--------------|-------|
|                            |              | False |
| RegistrationIdentification |              | False |
| TaxIdentification          |              | False |
| TaxType                    |              | False |
|                            |              | False |
| Authorisation              | TaxPartyRole | False |
| RegistrationIdentification |              | False |
| TaxIdentification          |              | False |
| TaxType                    |              | False |
|                            |              | False |
| FromToDate                 |              | False |
| Type                       |              | False |
| Year                       |              | False |
|                            |              | False |
| AdditionalInformation      |              | True  |
| Category                   |              | False |
| CategoryDetails            |              | True  |
| CertificateIdentification  |              | False |
|                            |              |       |

| TaxRecord3             | DebtorStatus         |                                | False | TaxRecord |
|------------------------|----------------------|--------------------------------|-------|-----------|
| TaxRecord3             | FormsCode            |                                | False | TaxRecord |
| TaxRecord3             | Period               | TaxPeriod                      | False | TaxRecord |
| TaxRecord3             | TaxAmount            | Tax                            | False | TaxRecord |
| TaxRecord3             | Type                 |                                | False | TaxRecord |
| TaxRecordDetails3      |                      |                                | False | Tax       |
| TaxRecordDetails3      | Amount               |                                | False | Tax       |
| TaxRecordDetails3      | Period               | TaxPeriod                      | True  |           |
| TransactionAllocation1 |                      |                                | False |           |
| TransactionAllocation1 | Account              | CashAccount                    | False | Payment   |
| TransactionAllocation1 | Amount               |                                | False |           |
| TransactionAllocation1 | CreditDebitIndicator |                                | False |           |
| TransactionAllocation1 | Purpose              | PaymentObligation              | False | Payment   |
| TransactionAllocation1 | Reference            |                                | False | Payment   |
| TransactionAllocation1 | RelatedReferences    | SecuritiesTradeIdentification  | False |           |
| TransactionParties11   |                      |                                | False |           |
| TransactionParties11   | Creditor             | PartyIdentificationInformation | False | Party     |
| TransactionParties11   | CreditorAccount      | CashAccount                    | False |           |
| TransactionParties11   | CreditorAgent        | Organisation                   | False |           |

| TransactionParties11 | CreditorAgentAccount             | CashAccount                    | False | PaymentPartyRole |
|----------------------|----------------------------------|--------------------------------|-------|------------------|
| TransactionParties11 | Debtor                           | PartyIdentificationInformation | False | Party            |
| TransactionParties11 | DebtorAccount                    | CashAccount                    | False | PaymentPartyRole |
| TransactionParties11 | DebtorAgent                      | Organisation                   | False | Party            |
| TransactionParties11 | DebtorAgentAccount               | CashAccount                    | False | PaymentPartyRole |
| TransactionParties11 | InitiatingParty                  | PartyIdentificationInformation | False | Party            |
| TransactionParties11 | IntermediaryAgent1               | Organisation                   | False | Organisation     |
| TransactionParties11 | IntermediaryAgent1Account        | CashAccount                    | False | PaymentPartyRole |
| TransactionParties11 | IntermediaryAgent2               | Organisation                   | False | Organisation     |
| TransactionParties11 | IntermediaryAgent2Account        | CashAccount                    | False | PaymentPartyRole |
| TransactionParties11 | IntermediaryAgent3               | Organisation                   | False | Organisation     |
| TransactionParties11 | IntermediaryAgent3Account        | CashAccount                    | False | PaymentPartyRole |
| TransactionParties11 | PreviousInstructingAgent1        | Organisation                   | False | Organisation     |
| TransactionParties11 | PreviousInstructingAgent1Account | CashAccount                    | False | PaymentPartyRole |
| TransactionParties11 | PreviousInstructingAgent2        | Organisation                   | False | Organisation     |
| TransactionParties11 | PreviousInstructingAgent2Account | CashAccount                    | False | PaymentPartyRole |

| TransactionParties11 | PreviousInstructingAgent3        | Organisation                   | False<br>Organisation     |
|----------------------|----------------------------------|--------------------------------|---------------------------|
| TransactionParties11 | PreviousInstructingAgent3Account | CashAccount                    | False<br>PaymentPartyRole |
| TransactionParties11 | UltimateCreditor                 | PartyIdentificationInformation | False<br>Party            |
| TransactionParties11 | UltimateDebtor                   | PartyIdentificationInformation | False<br>Party            |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |
|                      |                                  |                                |                           |

## **PaymentsClearingAndSettlement**