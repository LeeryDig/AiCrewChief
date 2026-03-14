# Engineer Signals Reference
Variáveis de telemetria do Automobilista 2 utilizadas pelo sistema de engenheiros.

Este documento define quais dados da shared memory são relevantes para:

- Practice Engineer (setup e comportamento do carro)
- Race Engineer (corrida e estratégia)

---

# Session Context (usado por ambos)

Essas variáveis permitem identificar o contexto da sessão.

- mSessionState
- mRaceState
- mSessionDuration
- mSessionAdditionalLaps
- mSessionIsPrivate

---

# PRACTICE ENGINEER
Engenheiro responsável por ajudar com comportamento do carro e sugestões de setup.

Usado em:

- Practice
- Test
- Qualifying

Objetivo:

Diagnosticar problemas de handling relatados pelo piloto.

---

## Comportamento do carro

- mSpeed
- mThrottle
- mBrake
- mSteering
- mGear
- mRpm

---

## Dinâmica do veículo

- mLocalVelocity
- mAngularVelocity
- mLocalAcceleration

---

## Suspensão

- mSuspensionTravel[]
- mSuspensionVelocity[]
- mRideHeight[]

---

## Pneus

- mTyreTemp[]
- mTyreTempLeft[]
- mTyreTempCenter[]
- mTyreTempRight[]
- mTyreWear[]
- mAirPressure[]
- mTyreCompound[][]

---

## Freios

- mBrakeTempCelsius[]
- mBrakeDamage[]

---

## Altura do carro

- mRideHeight[]

---

## Configuração atual do carro

- mBrakeBias
- mTractionControlSetting
- mAntiLockSetting
- mWings[]

---

## Danos

- mAeroDamage
- mEngineDamage
- mSuspensionDamage[]

---

## Condições da pista

- mTrackTemperature
- mAmbientTemperature
- mRainDensity

---

## Informações da pista

- mTrackLocation
- mTrackVariation
- mTrackLength

---

# RACE ENGINEER
Engenheiro responsável por corrida e estratégia.

Usado em:

- Race

Objetivo:

Gerenciar corrida, posição e estratégia.

---

## Estado da corrida

- mRaceState
- mCurrentLap
- mLapsInEvent
- mSessionDuration
- mEventTimeRemaining

---

## Posição

- mParticipantInfo[]
- mRaceStates[]
- mSpeeds[]

---

## Informações do jogador

- mViewedParticipantIndex
- mRacePosition

---

## Combustível

- mFuelLevel
- mFuelCapacity
- mFuelPressureKPa

---

## Voltas

- mLastLapTime
- mBestLapTime
- mCurrentTime

---

## Setores

- mCurrentSector1Time
- mCurrentSector2Time
- mCurrentSector3Time

---

## Tempo relativo

- mSplitTimeAhead
- mSplitTimeBehind

---

## Pneus (estratégia)

- mTyreWear[]
- mTyreTemp[]
- mTyreCompound[][]

---

## Pit

- mPitMode
- mPitSchedule
- mPitModes[]
- mPitSchedules[]
- mEnforcedPitStopLap

---

## Bandeiras

- mHighestFlagColour
- mHighestFlagReason
- mHighestFlagColours[]
- mHighestFlagReasons[]

---

## Safety Car / FCY

- mYellowFlagState

---

## Clima

- mRainDensity
- mTrackTemperature
- mAmbientTemperature
- mWindSpeed

---

## Energia / Sistemas

- mDrsState
- mErsDeploymentMode
- mErsAutoModeEnabled

---

# Possível expansão futura

O sistema pode futuramente usar:

- gaps reais entre carros
- previsão de combustível
- previsão de pit stop
- previsão de desgaste de pneus

---

# Estrutura sugerida no código

Practice engineer:

PracticeEngineer
→ usa dados de pneus
→ usa dados de suspensão
→ usa dados de dinâmica do carro

Race engineer:

RaceEngineer
→ usa dados de corrida
→ usa dados de posição
→ usa dados de estratégia