# Automobilista 2 — Shared Memory Reference

Este documento lista os campos disponíveis na estrutura `SharedMemory` utilizada pela API de telemetria do Automobilista 2.

A telemetria é baseada na mesma implementação usada no motor Madness (Project CARS).

---

# Versão / Build

- mVersion
- mBuildVersionNumber

---

# Estado do Jogo

- mGameState
- mSessionState
- mRaceState

---

# Participantes

- mViewedParticipantIndex
- mNumParticipants
- mParticipantInfo[]

ParticipantInfo contém:

- mIsActive
- mName
- mWorldPosition
- mCurrentLapDistance
- mRacePosition
- mLapsCompleted
- mCurrentLap
- mCurrentSector

---

# Inputs do Jogador (Unfiltered)

- mUnfilteredThrottle
- mUnfilteredBrake
- mUnfilteredSteering
- mUnfilteredClutch

---

# Informações do Veículo

- mCarName
- mCarClassName

---

# Informações do Evento

- mLapsInEvent
- mTrackLocation
- mTrackVariation
- mTrackLength

---

# Tempos e Voltas

- mNumSectors
- mLapInvalidated
- mBestLapTime
- mLastLapTime
- mCurrentTime
- mSplitTimeAhead
- mSplitTimeBehind
- mSplitTime
- mEventTimeRemaining
- mPersonalFastestLapTime
- mWorldFastestLapTime

---

# Tempos de Setor

- mCurrentSector1Time
- mCurrentSector2Time
- mCurrentSector3Time

- mFastestSector1Time
- mFastestSector2Time
- mFastestSector3Time

- mPersonalFastestSector1Time
- mPersonalFastestSector2Time
- mPersonalFastestSector3Time

- mWorldFastestSector1Time
- mWorldFastestSector2Time
- mWorldFastestSector3Time

---

# Bandeiras

- mHighestFlagColour
- mHighestFlagReason

---

# Pit

- mPitMode
- mPitSchedule

---

# Estado do Carro

- mCarFlags
- mOilTempCelsius
- mOilPressureKPa
- mWaterTempCelsius
- mWaterPressureKPa
- mFuelPressureKPa

---

# Combustível

- mFuelLevel
- mFuelCapacity

---

# Motor e Controles

- mSpeed
- mRpm
- mMaxRPM
- mBrake
- mThrottle
- mClutch
- mSteering
- mGear
- mNumGears

---

# Dados Gerais do Veículo

- mOdometerKM
- mAntiLockActive
- mLastOpponentCollisionIndex
- mLastOpponentCollisionMagnitude
- mBoostActive
- mBoostAmount

---

# Movimento do Carro

- mOrientation
- mLocalVelocity
- mWorldVelocity
- mAngularVelocity
- mLocalAcceleration
- mWorldAcceleration
- mExtentsCentre

---

# Pneus

- mTyreFlags[]
- mTerrain[]
- mTyreY[]
- mTyreRPS[]
- mTyreSlipSpeed
- mTyreTemp[]
- mTyreGrip
- mTyreHeightAboveGround[]
- mTyreLateralStiffness
- mTyreWear[]

---

# Freios

- mBrakeDamage[]
- mBrakeTempCelsius[]

---

# Suspensão

- mSuspensionDamage[]

---

# Temperatura dos Pneus

- mTyreTreadTemp[]
- mTyreLayerTemp[]
- mTyreCarcassTemp[]
- mTyreRimTemp[]
- mTyreInternalAirTemp[]

---

# Danos do Carro

- mCrashState
- mAeroDamage
- mEngineDamage

---

# Clima

- mAmbientTemperature
- mTrackTemperature
- mRainDensity
- mWindSpeed
- mWindDirectionX
- mWindDirectionY
- mCloudBrightness

---

# Controle de Integridade

- mSequenceNumber

---

# Posição das Rodas

- mWheelLocalPositionY[]

---

# Suspensão

- mSuspensionTravel[]
- mSuspensionVelocity[]

---

# Pressão

- mAirPressure[]

---

# Motor

- mEngineSpeed
- mEngineTorque

---

# Aerodinâmica

- mWings[]

---

# Freio de Mão

- mHandBrake

---

# Tempos dos Participantes

- mCurrentSector1Times[]
- mCurrentSector2Times[]
- mCurrentSector3Times[]

- mFastestSector1Times[]
- mFastestSector2Times[]
- mFastestSector3Times[]

- mFastestLapTimes[]
- mLastLapTimes[]

---

# Estados dos Participantes

- mLapsInvalidated[]
- mRaceStates[]
- mPitModes[]

---

# Orientação dos Participantes

- mOrientations[][]

---

# Velocidade dos Participantes

- mSpeeds[]

---

# Nome dos Carros dos Participantes

- mCarNames[]
- mCarClassNames[]

---

# Informações de Corrida

- mEnforcedPitStopLap

---

# Nomes Traduzidos da Pista

- mTranslatedTrackLocation
- mTranslatedTrackVariation

---

# Setup do Carro

- mBrakeBias
- mTurboBoostPressure

---

# Composto de Pneus

- mTyreCompound[][]

---

# Pit Schedules

- mPitSchedules[]

---

# Flags por Participante

- mHighestFlagColours[]
- mHighestFlagReasons[]

---

# Nacionalidade dos Pilotos

- mNationalities[]

---

# Clima Extra

- mSnowDensity

---

# Informações de Sessão

- mSessionDuration
- mSessionAdditionalLaps

---

# Temperatura do Pneu por Área

- mTyreTempLeft[]
- mTyreTempCenter[]
- mTyreTempRight[]

---

# DRS

- mDrsState

---

# Ride Height

- mRideHeight[]

---

# Input do Controle

- mJoyPad0
- mDPad

---

# Assistências

- mAntiLockSetting
- mTractionControlSetting

---

# ERS

- mErsDeploymentMode
- mErsAutoModeEnabled

---

# Embreagem

- mClutchTemp
- mClutchWear
- mClutchOverheated
- mClutchSlipping

---

# Bandeira Amarela

- mYellowFlagState

---

# Sessão

- mSessionIsPrivate

---

# Launch Control

- mLaunchStage